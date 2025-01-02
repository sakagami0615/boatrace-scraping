from dataclasses import dataclass


@dataclass
class BaseUrls:
    """ベースとなるURL情報"""
    RACE_INFO: str = "https://www.boatrace.jp/owpc/pc"


@dataclass
class StadiumUrls:
    """ボートレース場に関するURL情報
    jcd: 場コード
    """
    STADIUM_TOP: str = BaseUrls.RACE_INFO + "/extra/data/stadium/index.html"

    FMT_STADIUM: str = BaseUrls.RACE_INFO + "/data/stadium?jcd={:02}"


@dataclass
class RaceInfoUrls:
    """レース情報に関するURL情報
    rno: レース番号
    jcd: 場コード
    hd: 日付
    """
    FMT_RACE_CARD                : str = BaseUrls.RACE_INFO + "/race/racelist?rno={}&jcd={:02}&hd={:%Y%m%d}"            # 出走表
    FMT_ODDS_TRIFECTA            : str = BaseUrls.RACE_INFO + "/race/odds3t?rno={}&jcd={:02}&hd={:%Y%m%d}"              # オッズ：三連単
    FMT_ODDS_TRIO                : str = BaseUrls.RACE_INFO + "/race/odds3f?rno={}&jcd={:02}&hd={:%Y%m%d}"              # オッズ：三連複
    FMT_ODDS_EXACTA_AND_QUINELLA : str = BaseUrls.RACE_INFO + "/race/odds2tf?rno={}&jcd={:02}&hd={:%Y%m%d}"             # オッズ：二連単 / 二連複
    FMT_ODDS_QUINELLA_PLACE      : str = BaseUrls.RACE_INFO + "/race/oddsk?rno={}&jcd={:02}&hd={:%Y%m%d}"               # オッズ：拡連複
    FMT_ODDS_WIN_AND_PLACE       : str = BaseUrls.RACE_INFO + "/race/oddstf?rno={}&jcd={:02}&hd={:%Y%m%d}"              # オッズ：単勝 / 複勝
    FMT_BEFORE_INFO              : str = BaseUrls.RACE_INFO + "/race/beforeinfo?rno={}&jcd={:02}&hd={:%Y%m%d}"          # 直前情報
    FMT_RACE_RESULT              : str = BaseUrls.RACE_INFO + "/race/raceresult?rno={}&jcd={:02}&hd={:%Y%m%d}"          # 結果
    FMT_PIT_REPORT               : str = BaseUrls.RACE_INFO + "/race/pitreport?rno={}&jcd={:02}&hd={:%Y%m%d}"           # ピットレポート


@dataclass
class ScheduleUrls:
    """
    year: 開催年
    hdc: グレード
    """
    FMT_SCHEDULE: str = BaseUrls.RACE_INFO + "/race/gradesch?year={}&hcd={}"
