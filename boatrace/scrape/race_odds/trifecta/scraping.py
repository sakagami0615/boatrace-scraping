from typing import Any

from bs4.element import Tag
from datetime import datetime

from boatrace.common import split_list
from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.trifecta import OddsTrifectaColumns
from boatrace.scrape.race_odds.trifecta import OddsTrifectaConst
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM



class OddsTrifectaScraping:
    def __init__(self):
        pass

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_TRIFECTA.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

        td_soups = soup.find("tbody", class_=OddsTrifectaConst.tbody_class).find_all("td")
        line_td_soups = split_list(td_soups, n_div=TOOL_PARAM.n_racer - 1)

        scrape_datas = []
        for line_td_soup in line_td_soups:
            scrape_datas += self._extract_odds(race_id, stadium_id, date, line_td_soup)
        return scrape_datas

    def _extract_odds(self, race_id: int, stadium_id: int, date: datetime, line_td_soup: Tag) -> list[dict]:
        fs14_td_soups = [td_soup for td_soup in line_td_soup if OddsTrifectaConst.td_class in td_soup.attrs["class"]]
        td_soups      = [td_soup for td_soup in line_td_soup if OddsTrifectaConst.td_class not in td_soup.attrs["class"]]

        block_td_soups = []
        cell_td_soups = split_list(td_soups, n_div=len(td_soups) // 2)
        for block in range(TOOL_PARAM.n_racer):
            block_td_soups.append([td_soup for idx, td_soup in enumerate(cell_td_soups) if idx % TOOL_PARAM.n_racer == block])

        scrape_datas = []
        for idx_1st, (soup_2nd, soup_3rds) in enumerate(zip(fs14_td_soups, block_td_soups)):
            for no_soup, data_soup in soup_3rds:
                no_1st = idx_1st + 1
                no_2nd = soup_2nd.text.strip()
                no_3rd = no_soup.text.strip()

                bet_no = f"{no_1st},{no_2nd},{no_3rd}",
                odds = data_soup.text

                scrape_datas.append(OddsTrifectaColumns().cast([
                    race_id,
                    stadium_id,
                    date,
                    bet_no,
                    odds
                ]))
        return scrape_datas
