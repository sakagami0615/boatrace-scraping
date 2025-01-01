from datetime import datetime

from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.win import OddsWinColumns
from boatrace.scrape.race_odds.win import OddsWinConst
from boatrace.setting import CUSTOM_PARAM



class OddsWinScraping:
    def __init__(self):
        pass

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_WIN_AND_PLACE.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)
        win_table_soup, _ = soup.find_all("table", class_=OddsWinConst.table_class)

        tbody_soups = win_table_soup.find_all("tbody")

        scrape_datas = []
        for tbody_soup in tbody_soups:
            boat_no = tbody_soup.find("td", class_=OddsWinConst.boat_no_td_class).text
            odds = tbody_soup.find("td", class_=OddsWinConst.odds_td_class).text

            scrape_datas.append(OddsWinColumns().cast([
                race_id,
                stadium_id,
                date,
                boat_no,
                odds
            ]))
        return scrape_datas
