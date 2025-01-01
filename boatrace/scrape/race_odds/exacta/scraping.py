from datetime import datetime

from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.exacta import OddsExactaColumns
from boatrace.scrape.race_odds.exacta import OddsExactaConst
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM



class OddsExactaScraping:
    def __init__(self):
        pass

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_EXACTA_AND_QUINELLA.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)
        exacta_tbody_soup, _ = soup.find_all("tbody", class_=OddsExactaConst.tbody_class)

        tr_soups = exacta_tbody_soup.find_all("tr")

        scrape_datas = []
        for tr_soup in tr_soups:
            td_soups = tr_soup.find_all("td")
            for idx_1st in range(TOOL_PARAM.n_racer):
                no_1st = idx_1st + 1
                no_2nd = td_soups[idx_1st * 2].text.strip()

                bet_no = f"{no_1st},{no_2nd}"
                odds = td_soups[idx_1st * 2 + 1].text

                scrape_datas.append(OddsExactaColumns().cast([
                    race_id,
                    stadium_id,
                    date,
                    bet_no,
                    odds
                ]))
        return scrape_datas

