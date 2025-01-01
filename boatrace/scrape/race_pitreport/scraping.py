from bs4.element import Tag
from datetime import datetime

from boatrace.common import td_text_split
from boatrace.common import get_beautiful_soup

from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_pitreport import RacePitReportTdIndex
from boatrace.scrape.race_pitreport import RacePitReportRacerIndex
from boatrace.scrape.race_pitreport import RacePitReportConst
from boatrace.scrape.race_pitreport import RacePitReportColumns
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM



class RacePitReportScraping:

    def __init__(self):
        self._columns = RacePitReportColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_PIT_REPORT.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

        # [ピットレポートの表示対象レースではありません]と表示される場合は、空のデータを返却
        if not self._check_exist_pit_report(soup):
            empty_datas = []
            for _ in range(TOOL_PARAM.n_racer):
                empty_datas.append(self._create_empty__pit_report(race_id, stadium_id, date))
            return empty_datas

        table_soups = soup.find_all("div", class_=RacePitReportConst.table_class)
        tbody_soups = table_soups[-1].find_all("tbody")

        scrape_datas = []
        for tbody_soup in tbody_soups:
            scrape_datas.append(self._extract_pit_report(race_id, stadium_id, date, tbody_soup))
        return scrape_datas

    def _check_exist_pit_report(self, soup: Tag) -> bool:
        alert_soup = soup.find("h3", class_=RacePitReportConst.alert_class)
        return alert_soup is None

    def _create_empty__pit_report(self, race_id: int, stadium_id: int, date: datetime) -> dict:
        empty_datas = [None] * self._columns.n_columns
        empty_datas[0] = race_id
        empty_datas[1] = stadium_id
        empty_datas[2] = date
        return self._columns.cast(empty_datas)

    def _extract_pit_report(self, race_id: int, stadium_id: int, date: datetime, tbody_soup: Tag) -> dict:
        td_soups = tbody_soup.find_all("td")

        frame = td_soups[RacePitReportTdIndex.frame].text

        racer_data = td_text_split(td_soups[RacePitReportTdIndex.racer_status].text)
        racer_id = racer_data[RacePitReportRacerIndex.id]
        racer_class = racer_data[RacePitReportRacerIndex.cls]
        racer_name = racer_data[RacePitReportRacerIndex.name]
        racer_branch = racer_data[RacePitReportRacerIndex.branch]
        racer_birthplace = racer_data[RacePitReportRacerIndex.birthplace]
        racer_age = racer_data[RacePitReportRacerIndex.age]
        racer_weight = racer_data[RacePitReportRacerIndex.weight]

        pitreport = td_soups[RacePitReportTdIndex.pitreport].text
        before_result = td_soups[RacePitReportTdIndex.before_result].text

        return self._columns.cast([
            race_id,
            stadium_id,
            date,
            frame,
            racer_id,
            racer_class,
            racer_name,
            racer_branch,
            racer_birthplace,
            racer_age,
            racer_weight,
            pitreport,
            before_result,
        ])
