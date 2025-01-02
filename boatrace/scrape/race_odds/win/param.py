from dataclasses import dataclass


@dataclass
class OddsWinHtmlClass:
    table_class: str = "is-w495"
    boat_no_td_class: str = "is-fs14"
    odds_td_class: str = "oddsPoint"
