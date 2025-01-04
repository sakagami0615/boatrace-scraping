import pandas as pd

from boatrace.parameter import Grade
from boatrace.parameter import ScrapeKind
from boatrace.scrape.schedule import ScheduleScraping
from boatrace.scrape.race_card import RaceCardScraping
from boatrace.scrape.race_odds.trifecta import OddsTrifectaScraping
from boatrace.scrape.race_odds.trio import OddsTrioScraping
from boatrace.scrape.race_odds.win import OddsWinScraping
from boatrace.scrape.race_odds.place import OddsPlaceScraping
from boatrace.scrape.race_odds.quinella_place import OddsQuinellaPlaceScraping
from boatrace.scrape.race_odds.exacta import OddsExactaScraping
from boatrace.scrape.race_odds.quinella import OddsQuinellaScraping
from boatrace.scrape.race_before import RaceBeforeScraping
from boatrace.scrape.track import TrackScraping
from boatrace.scrape.race_pitreport import RacePitReportScraping
from boatrace.scrape.race_result import RaceResultScraping
from boatrace import BoatraceScraping


def sample_display_version():
    from boatrace import __version__
    print(f"version:{__version__}")


def sample_scrape_schedule(verbose=False):
    obj = ScheduleScraping()
    data = obj.scrape([2022, 2023], [g for g in Grade])
    df = pd.DataFrame(data)
    if verbose:
        print(df.head(3))
        print(df.shape)
    return df


def sample_scrape_race_card(schedule_df, verbose=False):
    obj = RaceCardScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_odds_trifecta(schedule_df, verbose=False):
    obj = OddsTrifectaScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_trio(schedule_df, verbose=False):
    obj = OddsTrioScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_odds_win(schedule_df, verbose=False):
    obj = OddsWinScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_odds_place(schedule_df, verbose=False):
    obj = OddsPlaceScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_odds_quinella_place(schedule_df, verbose=False):
    obj = OddsQuinellaPlaceScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_odds_exacta(schedule_df, verbose=False):
    obj = OddsExactaScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_odds_quinella(schedule_df, verbose=False):
    obj = OddsQuinellaScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_race_before(schedule_df, verbose=False):
    obj = RaceBeforeScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_track(verbose=False):
    obj = TrackScraping()
    course_datas, frame_datas, season_datas, memo_datas = obj.scrape()

    df_course = pd.DataFrame(course_datas)
    df_frame = pd.DataFrame(frame_datas)
    df_season = pd.DataFrame(season_datas)
    df_memo = pd.DataFrame(memo_datas)

    if verbose:
        print("df_course")
        print(df_course)
        print(df_course.shape)
        print("df_frame")
        print(df_frame)
        print(df_frame.shape)
        print("df_season")
        print(df_season)
        print(df_season.shape)
        print("df_memo")
        print(df_memo)
        print(df_memo.shape)


def sample_scrape_pit_report(schedule_df, verbose=False):
    obj = RacePitReportScraping()
    data = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df = pd.DataFrame(data)
    if verbose:
        print(df)
        print(df.shape)


def sample_scrape_race_result(schedule_df, verbose=False):
    obj = RaceResultScraping()
    result_datas, return_datas = obj.scrape(
        schedule_df["レース番号"].iloc[0],
        schedule_df["レース場ID"].iloc[0],
        schedule_df["開催日程"].iloc[0]
    )
    df_result = pd.DataFrame(result_datas)
    df_return = pd.DataFrame(return_datas)
    if verbose:
        print(df_result)
        print(df_return)


def sample_scrape_boatrace():
    boatrace_scape = BoatraceScraping()
    #boatrace_scape.scrape(2022, scrape_kinds=ScrapeKind.race_card)
    boatrace_scape.scrape([2022, 2023, 2024])


if __name__ == "__main__":
    #sample_display_version()

    #schedule_df = sample_scrape_schedule(verbose=False)
    #sample_scrape_race_card(schedule_df, verbose=False)
    #sample_scrape_odds_trifecta(schedule_df, verbose=False)
    #sample_scrape_trio(schedule_df, verbose=False)
    #sample_scrape_odds_win(schedule_df, verbose=False)
    #sample_scrape_odds_place(schedule_df, verbose=False)
    #sample_scrape_odds_quinella_place(schedule_df, verbose=False)
    #sample_scrape_odds_exacta(schedule_df, verbose=False)
    #sample_scrape_odds_quinella(schedule_df, verbose=False)
    #sample_scrape_race_before(schedule_df, verbose=False)
    #sample_scrape_track(verbose=False)
    #sample_scrape_pit_report(schedule_df, verbose=False)
    #sample_scrape_race_result(schedule_df, verbose=False)

    sample_scrape_boatrace()
