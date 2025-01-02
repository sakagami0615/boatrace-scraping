from dataclasses import dataclass, field

from boatrace.common import ColumnsMixin
from boatrace.common import ColumnDatatype
from boatrace.common.cast_function import Datetime


@dataclass
class ScheduleColumns(ColumnsMixin):
    race_no:    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース番号", int))
    stadium_id: ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    date:       ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催日程", Datetime))
    grade:      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("グレード", str))
    timezone:   ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催時間帯", str))
    title:      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("タイトル", str))
    is_held:    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催済", bool))
