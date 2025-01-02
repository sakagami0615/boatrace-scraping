from dataclasses import dataclass


@dataclass
class TrackHtmlClass:
    table_class: str = "tableType4"


@dataclass
class Latest3MonthCourseResultHtmlClass:
    table_class: str = "is-w748"


@dataclass
class Latest3MonthFrameResultHtmlClass:
    table_class: str = "is-w413"


@dataclass
class SeasonResultHtmlClass:
    table_class: str = "is-w358"


@dataclass
class MemoHtmlClass:
    table_class: str = "frame10_inner"
