from dataclasses import dataclass, field

from boatrace.common import ColumnsMixin
from boatrace.common import ColumnDatatype
from boatrace.common.cast_function import Datetime, Name, Age, Weight


@dataclass
class RacePitReportColumns(ColumnsMixin):
    race_id:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レースID", int))
    stadium_id:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    date:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催日程", Datetime))
    frame:              ColumnDatatype = field(default_factory=lambda: ColumnDatatype("枠", int))
    racer_id:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-登録番号", int))
    racer_class:        ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-級別", str))
    racer_name:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-氏名", Name))
    racer_branch:       ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-支部", str))
    racer_birthplace:   ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-出身地", str))
    racer_age:          ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-年齢", Age))
    racer_weight:       ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-体重", Weight))
    pitreport:          ColumnDatatype = field(default_factory=lambda: ColumnDatatype("ピットレポート", str))
    before_result:      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("前走結果", str))

