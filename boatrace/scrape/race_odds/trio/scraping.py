from bs4.element import Tag
from datetime import datetime

from boatrace.common import split_list
from boatrace.common import get_beautiful_soup
from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_odds.trio import OddsTrioTableInfoInHtml
from boatrace.scrape.race_odds.trio import OddsTrioHtmlClass
from boatrace.scrape.race_odds.trio import OddsTrioColumns
from boatrace.setting import CUSTOM_PARAM


class OddsTrioScraping:
    """3連複オッズのスクレイピング"""

    def __init__(self):
        self._column = OddsTrioColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_ODDS_TRIO.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)
        td_soups = soup.find("tbody", class_=OddsTrioHtmlClass.tbody_class).find_all("td")

        group_no_list = []
        for group_no, idx in enumerate(reversed(range(OddsTrioTableInfoInHtml.line_row_size))):
            n_items = OddsTrioTableInfoInHtml.n_head_items + OddsTrioTableInfoInHtml.n_line_items * idx
            group_no_list.extend([group_no] * n_items)

        line_td_soups = [[] for _ in range(OddsTrioTableInfoInHtml.line_row_size)]
        for group_no, td_soup in zip(group_no_list, td_soups):
            line_td_soups[group_no].append(td_soup)

        scrape_datas = []
        for idx_line, line_td_soup in enumerate(line_td_soups):
            scrape_datas += self._extract_odds(race_id, stadium_id, date, line_td_soup, idx_line)
        return scrape_datas

    def _extract_odds(self, race_id: int, stadium_id: int, date: datetime, line_td_soup: Tag, idx_line: int) -> list[dict]:
        n_block = idx_line + 1
        fs14_td_soups = [td_soup for td_soup in line_td_soup if OddsTrioHtmlClass.td_class in td_soup.attrs["class"]]
        td_soups = [td_soup for td_soup in line_td_soup if (OddsTrioHtmlClass.td_class not in td_soup.attrs["class"] and
                                                            OddsTrioHtmlClass.disable_class not in td_soup.attrs["class"])]

        cell_td_soups = split_list(td_soups, n_div=len(td_soups) // 2)
        block_td_soups = [[td_soup for idx, td_soup in enumerate(cell_td_soups) if idx % n_block == block] for block in range(n_block)]

        scrape_datas = []
        for idx_1st, (soup_2nd, soup_3rds) in enumerate(zip(fs14_td_soups, block_td_soups)):
            for no_soup, data_soup in soup_3rds:
                no_1st = idx_1st + 1
                no_2nd = soup_2nd.text.strip()
                no_3rd = no_soup.text.strip()

                bet_no = f"{no_1st},{no_2nd},{no_3rd}",
                odds = data_soup.text

                scrape_datas.append(self._column.cast([
                    race_id,
                    stadium_id,
                    date,
                    bet_no,
                    odds
                ]))
        return scrape_datas
