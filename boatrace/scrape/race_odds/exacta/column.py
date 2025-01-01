from dataclasses import dataclass, field

from boatrace.common import ColumnsMixin
from boatrace.common import ColumnDatatype
from boatrace.common.cast_function import Datetime, List



@dataclass
class OddsExactaColumns(ColumnsMixin):
    race_id:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レースID", int))
    stadium_id:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    date:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催日程", Datetime))
    bet_no:             ColumnDatatype = field(default_factory=lambda: ColumnDatatype("組番", List))
    odds:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("オッズ", float))
