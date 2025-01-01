from dataclasses import dataclass


@dataclass
class TrackConst:
    table_class: str = "tableType4"


@dataclass
class Latest3MonthCourseResultConst:
    table_class: str = "is-w748"


@dataclass
class Latest3MonthFrameResultConst:
    table_class: str = "is-w413"


@dataclass
class SeasonResultConst:
    table_class: str = "is-w358"


@dataclass
class MemoConst:
    table_class: str = "frame10_inner"
