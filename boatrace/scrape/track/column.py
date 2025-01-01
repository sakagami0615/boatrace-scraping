from dataclasses import dataclass, field

from boatrace.common import ColumnsMixin
from boatrace.common import ColumnDatatype



@dataclass
class Latest3MonthCourseResultColumns(ColumnsMixin):
    stadium_id:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    course:                     ColumnDatatype = field(default_factory=lambda: ColumnDatatype("コース", int))
    rank1:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("1着", float))
    rank2:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("2着", float))
    rank3:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("3着", float))
    rank4:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("4着", float))
    rank5:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("5着", float))
    rank6:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("6着", float))
    wintric_escape:             ColumnDatatype = field(default_factory=lambda: ColumnDatatype("逃げ", float))
    wintric_turnover:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("捲り", float))
    wintric_insert:             ColumnDatatype = field(default_factory=lambda: ColumnDatatype("差し", float))
    wintric_turnover_insert:    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("捲り差し", float))
    wintric_overtake:           ColumnDatatype = field(default_factory=lambda: ColumnDatatype("抜き", float))
    wintric_blessed:            ColumnDatatype = field(default_factory=lambda: ColumnDatatype("恵まれ", float))


@dataclass
class Latest3MonthFrameResultColumns(ColumnsMixin):
    stadium_id:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    frame:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("枠", int))
    course1:                    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("1コース", float))
    course2:                    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("2コース", float))
    course3:                    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("3コース", float))
    course4:                    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("4コース", float))
    course5:                    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("5コース", float))
    course6:                    ColumnDatatype = field(default_factory=lambda: ColumnDatatype("6コース", float))


@dataclass
class SeasonResultColumns(ColumnsMixin):
    stadium_id:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    course:                     ColumnDatatype = field(default_factory=lambda: ColumnDatatype("コース", int))
    spring_rank1:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("春季-1着", float))
    spring_rank2:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("春季-2着", float))
    spring_rank3:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("春季-3着", float))
    spring_rank4:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("春季-4着", float))
    spring_rank5:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("春季-5着", float))
    spring_rank6:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("春季-6着", float))
    summer_rank1:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("夏季-1着", float))
    summer_rank2:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("夏季-2着", float))
    summer_rank3:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("夏季-3着", float))
    summer_rank4:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("夏季-4着", float))
    summer_rank5:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("夏季-5着", float))
    summer_rank6:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("夏季-6着", float))
    autumn_rank1:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("秋季-1着", float))
    autumn_rank2:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("秋季-2着", float))
    autumn_rank3:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("秋季-3着", float))
    autumn_rank4:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("秋季-4着", float))
    autumn_rank5:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("秋季-5着", float))
    autumn_rank6:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("秋季-6着", float))
    winter_rank1:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("冬季-1着", float))
    winter_rank2:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("冬季-2着", float))
    winter_rank3:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("冬季-3着", float))
    winter_rank4:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("冬季-4着", float))
    winter_rank5:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("冬季-5着", float))
    winter_rank6:               ColumnDatatype = field(default_factory=lambda: ColumnDatatype("冬季-6着", float))


@dataclass
class MemoColumns(ColumnsMixin):
    stadium_id:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レース場ID", int))
    place:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("所在地", str))
    motor:                      ColumnDatatype = field(default_factory=lambda: ColumnDatatype("モーター", str))
    water_quality:              ColumnDatatype = field(default_factory=lambda: ColumnDatatype("水質", str))
    tidal_diff:                 ColumnDatatype = field(default_factory=lambda: ColumnDatatype("干満差", str))
    record:                     ColumnDatatype = field(default_factory=lambda: ColumnDatatype("レコード", str))
