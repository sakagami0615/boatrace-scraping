from dataclasses import dataclass, field

from boatrace.common import ColumnsMixin
from boatrace.common import ColumnDatatype
from boatrace.common.cast_function import Datetime, Name, Weight, Temperature, Distance, StartTiming



@dataclass
class RaceBeforeColumns(ColumnsMixin):
    race_id:                ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レースID", int))
    stadium_id:             ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    date:                   ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催日程", Datetime))
    frame:                  ColumnDatatype = field(default_factory=lambda: ColumnDatatype("枠", int))
    name:                   ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-氏名", Name))
    weight:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-体重", Weight))
    adjust_weight:          ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-調整体重", float))
    exhibit_time:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("展示タイム", int))
    tilt:                   ColumnDatatype = field(default_factory=lambda: ColumnDatatype("チルト", int))
    propeller:              ColumnDatatype = field(default_factory=lambda: ColumnDatatype("プロペラ", str))
    parts_replace:          ColumnDatatype = field(default_factory=lambda: ColumnDatatype("部品交換", str))
    before_result_r:        ColumnDatatype = field(default_factory=lambda: ColumnDatatype("前走成績-R", int))
    before_result_entry:    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("前走成績-進入", float))
    before_result_st:       ColumnDatatype = field(default_factory=lambda: ColumnDatatype("前走成績-ST", float))
    before_result_rank:     ColumnDatatype = field(default_factory=lambda: ColumnDatatype("前走成績-着順", int))
    st:                     ColumnDatatype = field(default_factory=lambda: ColumnDatatype("ST", StartTiming))
    temperature:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("気温", Temperature))
    weather:                ColumnDatatype = field(default_factory=lambda: ColumnDatatype("天気", str))
    wind_velocity:          ColumnDatatype = field(default_factory=lambda: ColumnDatatype("風速", Distance))
    wind_direction:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("風向", str))
    water_temperature:      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("水温", Temperature))
    wave_height:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("波高", Distance))
