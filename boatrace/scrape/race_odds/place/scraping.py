from datetime import datetime

from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.place import OddsPlaceHtmlClass
from boatrace.scrape.race_odds.place import OddsPlaceColumns
from boatrace.setting import CUSTOM_PARAM


class OddsPlaceScraping:
    """複勝オッズのスクレイピング"""

    def __init__(self):
        self._column = OddsPlaceColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_WIN_AND_PLACE.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)
        _, place_table_soup = soup.find_all("table", class_=OddsPlaceHtmlClass.table_class)

        tbody_soups = place_table_soup.find_all("tbody")

        scrape_datas = []
        for tbody_soup in tbody_soups:
            boat_no = tbody_soup.find("td", class_=OddsPlaceHtmlClass.boat_no_td_class).text
            minmax_odds = tbody_soup.find("td", class_=OddsPlaceHtmlClass.odds_td_class).text.strip().split("-")

            scrape_datas.append(self._column.cast([
                race_id,
                stadium_id,
                date,
                boat_no,
                minmax_odds[0],
                minmax_odds[1]
            ]))
        return scrape_datas