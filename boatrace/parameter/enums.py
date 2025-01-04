from enum import Enum


class Grade(Enum):
    """レースグレードIDの定義クラス"""
    SgPg1  = "01"
    G1G2   = "02"
    G3     = "03"
    Venus  = "04"
    Rookie = "05"
    Master = "06"


class ScrapeKind(Enum):
    """スクレイピング対象の定義クラス"""
    track = 0
    race_before = 1
    race_card = 2
    race_pitreport = 3
    race_result = 4
    odds_trifecta = 5
    odds_trio = 6
    odds_exacta = 7
    odds_quinella = 8
    odds_quinellaPlace = 9
    odds_win = 10
    odds_place = 11
