from dataclasses import dataclass


@dataclass
class RacePitReportTdIndex:
    frame: int = 0
    racer_status: int = 2
    pitreport: int = 3
    before_result: int = 4


@dataclass
class RacePitReportRacerIndex:
    id: int = 0
    cls: int = 1
    name: int = 2
    branch: int = 3
    birthplace: int = 4
    age: int = 5
    weight: int = 6


@dataclass
class RacePitReportHtmlClass:
    table_class: str = "table1"
    alert_class: str = "title12_title"
