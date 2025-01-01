from bs4.element import Tag
from datetime import datetime

from boatrace.common import td_text_split
from boatrace.common import get_beautiful_soup

from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_card import RaceCardTdIndex
from boatrace.scrape.race_card import RaceCardRacerIndex
from boatrace.scrape.race_card import RaceCardWideIndex
from boatrace.scrape.race_card import RaceCardLocalIndex
from boatrace.scrape.race_card import RaceCardMotorIndex
from boatrace.scrape.race_card import RaceCardBoatIndex
from boatrace.scrape.race_card import RaceCardConst
from boatrace.scrape.race_card import RaceCardColumns
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM



class RaceCardScraping:

    def __init__(self):
        self._column = RaceCardColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_RACE_CARD.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

        table_soup = soup.find("div", class_=RaceCardConst.table_class).find("table")
        tbody_soups = table_soup.find_all("tbody", class_=RaceCardConst.tbody_class)

        scrape_datas = []
        for tbody_soup in tbody_soups:
            scrape_datas.append(self._extract_racer_info(race_id, stadium_id, date, tbody_soup))
        return scrape_datas

    def _extract_racer_info(self, race_id: int, stadium_id: int, date: datetime, tbody_soup: Tag) -> list[dict]:
        td_soups = tbody_soup.find_all("td")

        frame = td_soups[RaceCardTdIndex.frame].text
        racer_data = td_text_split(td_soups[RaceCardTdIndex.racer_status].text) + td_text_split(td_soups[RaceCardTdIndex.racer_score].text)
        wide_data = td_text_split(td_soups[RaceCardTdIndex.wide].text)
        local_data = td_text_split(td_soups[RaceCardTdIndex.local].text)
        motor_data = td_text_split(td_soups[RaceCardTdIndex.motor].text)
        boat_data = td_text_split(td_soups[RaceCardTdIndex.boat].text)

        def get_racer_info():
            return [racer_data[RaceCardRacerIndex.id],
                    racer_data[RaceCardRacerIndex.cls],
                    racer_data[RaceCardRacerIndex.name],
                    racer_data[RaceCardRacerIndex.branch],
                    racer_data[RaceCardRacerIndex.birthplace],
                    racer_data[RaceCardRacerIndex.age],
                    racer_data[RaceCardRacerIndex.weight],
                    racer_data[RaceCardRacerIndex.fn],
                    racer_data[RaceCardRacerIndex.ln],
                    racer_data[RaceCardRacerIndex.avgst]]

        def get_wide():
            return [wide_data[RaceCardWideIndex.rate1],
                    wide_data[RaceCardWideIndex.rate2],
                    wide_data[RaceCardWideIndex.rate3]]

        def get_local():
            return [local_data[RaceCardLocalIndex.rate1],
                    local_data[RaceCardLocalIndex.rate2],
                    local_data[RaceCardLocalIndex.rate3]]

        def get_motor():
            return [motor_data[RaceCardMotorIndex.no],
                    motor_data[RaceCardMotorIndex.rate2],
                    motor_data[RaceCardMotorIndex.rate3]]

        def get_boat():
            return [boat_data[RaceCardBoatIndex.no],
                    boat_data[RaceCardBoatIndex.rate2],
                    boat_data[RaceCardBoatIndex.rate3]]

        def get_last_result(idx):
            row_width = TOOL_PARAM.n_max_day * 2
            return [td_soups[RaceCardTdIndex.result + idx + row_width * 0].text,
                    td_soups[RaceCardTdIndex.result + idx + row_width * 1 + 1].text,
                    td_soups[RaceCardTdIndex.result + idx + row_width * 2 + 1].text,
                    td_soups[RaceCardTdIndex.result + idx + row_width * 3 + 1].text]

        card_datas = [race_id, stadium_id, date, frame]
        card_datas += get_racer_info()
        card_datas += get_wide()
        card_datas += get_local()
        card_datas += get_motor()
        card_datas += get_boat()

        for idx in range(TOOL_PARAM.n_max_day * 2):
            card_datas += get_last_result(idx)

        return self._column.cast(card_datas)
