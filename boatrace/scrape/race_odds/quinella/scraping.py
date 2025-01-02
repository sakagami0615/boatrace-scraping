from datetime import datetime

from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.quinella import OddsQuinellaHtmlClass
from boatrace.scrape.race_odds.quinella import OddsQuinellaColumns
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM


class OddsQuinellaScraping:
    """2連複オッズのスクレイピング"""

    def __init__(self):
        self._column = OddsQuinellaColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_EXACTA_AND_QUINELLA.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)
        _, quinella_tbody_soup = soup.find_all("tbody", class_=OddsQuinellaHtmlClass.tbody_class)

        tr_soups = quinella_tbody_soup.find_all("tr")

        scrape_datas = []
        for tr_soup in tr_soups:
            td_soups = tr_soup.find_all("td")
            for idx_1st in range(TOOL_PARAM.n_racer):
                no_1st = idx_1st + 1
                no_2nd = td_soups[idx_1st * 2].text.strip()

                bet_no = f"{no_1st},{no_2nd}"
                odds = td_soups[idx_1st * 2 + 1].text.strip()

                if odds:
                    scrape_datas.append(self._column.cast([
                        race_id,
                        stadium_id,
                        date,
                        bet_no,
                        odds
                    ]))
        return scrape_datas

