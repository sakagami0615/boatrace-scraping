from dataclasses import dataclass


@dataclass
class RaceBeforeRacerStatusIndex:
    frame: int = 0
    name: int = 2
    weight: int = 3
    adjust_weight: int = 12
    exhibit_time: int = 4
    tilt: int = 5
    propeller: int = 6
    parts_replace: int = 7
    before_result_r: int = 9
    before_result_entry: int = 11
    before_result_st: int = 14
    before_result_rank: int = 16


@dataclass
class RaceBeforeWeatherIndex:
    temperature: int = 0
    weather: int = 1
    wind_velocity: int = 2
    wind_direction: int = 3
    water_temperature: int = 4
    wave_height: int = 5


@dataclass
class RaceBeforeHtmlClass:
    absent_tbody_class: str = "is-miss"
    racer_table_class: str = "is-w748"
    start_table_class: str = "is-w238"
    weather_div_class: str = "weather1"
    start_tr_class: str = "table1_boatImage1Time"

    weather_bodyunit_class: str = "weather1_bodyUnit"
    temperature_class: str = "weather1_bodyUnitLabelData"
    weather_class: str = "weather1_bodyUnitLabelTitle"
    wind_velocity_class: str = "weather1_bodyUnitLabelData"
    water_temperature_class: str = "weather1_bodyUnitLabelData"
    wave_height_class: str = "weather1_bodyUnitLabelData"
