from typing import Union

import os
import pandas as pd
from tqdm import tqdm

from boatrace.common import write_pickle
from boatrace.parameter import Grade
from boatrace.parameter import ScrapeKind
from boatrace.scrape.race_before import RaceBeforeScraping
from boatrace.scrape.race_card import RaceCardScraping
from boatrace.scrape.race_odds.exacta import OddsExactaScraping
from boatrace.scrape.race_odds.place import OddsPlaceScraping
from boatrace.scrape.race_odds.quinella import OddsQuinellaScraping
from boatrace.scrape.race_odds.quinella_place import OddsQuinellaPlaceScraping
from boatrace.scrape.race_odds.trifecta import OddsTrifectaScraping
from boatrace.scrape.race_odds.trio import OddsTrioScraping
from boatrace.scrape.race_odds.win import OddsWinScraping
from boatrace.scrape.race_pitreport import RacePitReportScraping
from boatrace.scrape.race_result import RaceResultScraping
from boatrace.scrape.schedule import ScheduleScraping
from boatrace.scrape.track import TrackScraping
from boatrace.scrape.schedule import ScheduleColumns
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM, CUSTOM_LOGGER


logger = CUSTOM_LOGGER.create_logger(TOOL_PARAM.tool_name)


class BoatraceScraping:
    """ボートレース情報のスクレイピング"""

    def __init__(self):
        pass

    def _create_race_scrape(self) -> dict:
        return {
            ScrapeKind.race_before: RaceBeforeScraping(),
            ScrapeKind.race_card: RaceCardScraping(),
            ScrapeKind.race_pitreport: RacePitReportScraping(),
            ScrapeKind.race_result: RaceResultScraping(),
            ScrapeKind.odds_trifecta: OddsExactaScraping(),
            ScrapeKind.odds_trio: OddsPlaceScraping(),
            ScrapeKind.odds_exacta: OddsQuinellaScraping(),
            ScrapeKind.odds_quinella: OddsQuinellaPlaceScraping(),
            ScrapeKind.odds_quinellaPlace: OddsTrifectaScraping(),
            ScrapeKind.odds_win: OddsTrioScraping(),
            ScrapeKind.odds_place: OddsWinScraping()
        }

    def scrape(self, years: Union[int, list[int]],
                     grade_types: Union[Grade, list[Grade], None]=None,
                     scrape_kinds: Union[ScrapeKind, list[ScrapeKind], None]=None) -> None:
        """競艇データのスクレイピング"""

        if not isinstance(years, list):
            years = [years]

        if grade_types is None:
            grade_types = [v for v in list(Grade)]
        elif not isinstance(grade_types, list):
            grade_types = [grade_types]

        if scrape_kinds is None:
            scrape_kinds = [v for v in list(ScrapeKind)]
        elif not isinstance(scrape_kinds, list):
            scrape_kinds = [scrape_kinds]

        # コース場情報のスクレイピングば別メソッドを使用するため、指定されているかを検出しておき、
        # popすることでレース情報のスクレイピングの引数に入らないようにする
        is_scrape_track = False
        if ScrapeKind.track in scrape_kinds:
            is_scrape_track = True
            scrape_kinds.remove(ScrapeKind.track)

        # コース場とレースの情報をスクレイピング
        scrape_dfs = {}
        if is_scrape_track:
            logger.info("scraping track info")
            scrape_dfs |= self._scrape_track_info()
        if len(scrape_kinds) > 0:
            logger.info("scraping race info")
            scrape_dfs |= self._scrape_race_info(years, grade_types, scrape_kinds)

        # スクレイピングデータの保存
        logger.info("save scraping datas")
        os.makedirs(CUSTOM_PARAM.output_folder, exist_ok=True)
        with tqdm(scrape_dfs.items()) as bar:
            for scrape_kind, scrape_df in bar:
                bar.set_description(f"[Save-{scrape_kind.value}]")
                name = scrape_kind._name_
                write_pickle(os.path.join(CUSTOM_PARAM.output_folder, f"{name}.pickle"), scrape_df)
                scrape_df.to_csv(os.path.join(CUSTOM_PARAM.output_folder, f"{name}.csv"), index=False)

    def _scrape_track_info(self) -> dict:
        """コース場情報のスクレイピング"""
        track = TrackScraping()
        return {
            ScrapeKind.track: pd.DataFrame(track.scrape())
        }

    def _scrape_race_info(self, years: list[int], grade_types: list[Grade], scrape_kinds: list[ScrapeKind]) -> dict:
        """レース情報のスクレイピング"""
        schedule_scrape = ScheduleScraping()
        schedule_column = ScheduleColumns()
        race_scrape = self._create_race_scrape()

        schedule_df = pd.DataFrame(schedule_scrape.scrape(years, grade_types))
        race_nos = schedule_df[schedule_column.race_no.name]
        stadium_ids = schedule_df[schedule_column.stadium_id.name]
        dates = schedule_df[schedule_column.date.name]

        scrape_dfs = {scrape_kind: None for scrape_kind in scrape_kinds}

        with tqdm(zip(race_nos, stadium_ids, dates), total=len(race_nos)) as race_bar:
            for race_no, stadium_id, date in race_bar:
                date_str = date.strftime("%Y%m%d")
                race_bar.set_description(f"[RaceIter-{race_no}-{stadium_id}-{date_str}]")

                with tqdm(scrape_kinds, leave=False) as kind_bar:
                    for scrape_kind in kind_bar:
                        kind_bar.set_description(f"[ScrapeKind-{scrape_kind.value}]")

                        scape_datas = race_scrape[scrape_kind].scrape(race_no, stadium_id, date)
                        scrape_df = pd.DataFrame(scape_datas)

                        if scrape_dfs[scrape_kind] is None:
                            scrape_dfs[scrape_kind] = scrape_df
                        else:
                            scrape_dfs[scrape_kind] = pd.concat([scrape_dfs[scrape_kind], scrape_df], axis=0, ignore_index=True)

        return scrape_dfs
