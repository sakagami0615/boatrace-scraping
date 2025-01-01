from dataclasses import dataclass, field

from boatrace.common import ColumnsMixin
from boatrace.common import ColumnDatatype
from boatrace.common.cast_function import Datetime, Name, Temperature, Distance, StartTiming, Money



@dataclass
class RaceResultColumns(ColumnsMixin):
    race_id:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レースID", int))
    stadium_id:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    date:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催日程", Datetime))
    rank:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("着", int))
    frame:              ColumnDatatype = field(default_factory=lambda: ColumnDatatype("枠", int))
    racer_id:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-登録番号", int))
    racer_name:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レーサ-氏名", Name))
    racetime:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レースタイム", str))
    st:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("ST", StartTiming))
    temperature:        ColumnDatatype = field(default_factory=lambda: ColumnDatatype("気温", Temperature))
    weather:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("天気", str))
    wind_velocity:      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("風速", Distance))
    wind_direction:     ColumnDatatype = field(default_factory=lambda: ColumnDatatype("風向", str))
    water_temperature:  ColumnDatatype = field(default_factory=lambda: ColumnDatatype("水温", Temperature))
    wave_height:        ColumnDatatype = field(default_factory=lambda: ColumnDatatype("波高", Distance))
    restoration:        ColumnDatatype = field(default_factory=lambda: ColumnDatatype("返還", str))
    wintric:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("決まり手", str))


@dataclass
class RaceReturnColumns(ColumnsMixin):
    race_id:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レースID", int))
    stadium_id:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    date:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("開催日程", Datetime))
    bet_type:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("勝式", str))
    bet_number:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("組番", str))
    return_money:       ColumnDatatype = field(default_factory=lambda: ColumnDatatype("払戻金", Money))
    popularity:         ColumnDatatype = field(default_factory=lambda: ColumnDatatype("人気", int))
