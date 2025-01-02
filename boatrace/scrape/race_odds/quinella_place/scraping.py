from bs4.element import Tag
from datetime import datetime

from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.quinella_place import OddsQuinellaPlaceHtmlClass
from boatrace.scrape.race_odds.quinella_place import OddsQuinellaPlaceColumns
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM


class OddsQuinellaPlaceScraping:
    """拡連複オッズのスクレイピング"""

    def __init__(self):
        self._column = OddsQuinellaPlaceColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_QUINELLA_PLACE.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)
        tbody_soup = soup.find("tbody", class_=OddsQuinellaPlaceHtmlClass.tbody_class)

        tr_soups = tbody_soup.find_all("tr")

        scrape_datas = []
        for tr_soup in tr_soups:
            scrape_datas += self._extract_odds(race_id, stadium_id, date, tr_soup)
        return scrape_datas

    def _extract_odds(self, race_id: int, stadium_id: int, date: datetime, tr_soup: Tag) -> list[dict]:
        td_soups = tr_soup.find_all("td")

        scrape_datas = []
        for idx_1st in range(TOOL_PARAM.n_racer):
            no_1st = idx_1st + 1
            no_2nd = td_soups[idx_1st * 2].text.strip()

            bet_no = f"{no_1st},{no_2nd}"
            minmax_odds = td_soups[idx_1st * 2 + 1].text.strip().split("-")

            if minmax_odds != [""]:
                scrape_datas.append(self._column.cast([
                    race_id,
                    stadium_id,
                    date,
                    bet_no,
                    minmax_odds[0],
                    minmax_odds[1]
                ]))
        return scrape_datas
