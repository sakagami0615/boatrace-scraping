from dataclasses import dataclass


@dataclass
class RaceResultReturnTableInfoInHtml:
    n_cols: int = 4


@dataclass
class RaceResultTimeIndex:
    rank: int = 0
    frame: int = 1
    racer: int = 2
    racetime: int = 3


@dataclass
class RaceResultWeatherIndex:
    temperature: int = 0
    weather: int = 1
    wind_velocity: int = 2
    wind_direction: int = 3
    water_temperature: int = 4
    wave_height: int = 5


@dataclass
class RaceResultReturnIndex:
    bet_number: int = 0
    return_money: int = 1
    popularity: int = 2


@dataclass
class RaceResultConst:
    result_table_class: str = "is-w495"
    weather_table_class: str = "weather1"
    wintric_div_class: str = "is-h108__3rdadd"

    st_class: str = "table1_boatImage1TimeInner"

    weather_bodyunit_class: str = "weather1_bodyUnit"
    temperature_class: str = "weather1_bodyUnitLabelData"
    weather_class: str = "weather1_bodyUnitLabelTitle"
    wind_velocity_class: str = "weather1_bodyUnitLabelData"
    water_temperature_class: str = "weather1_bodyUnitLabelData"
    wave_height_class: str = "weather1_bodyUnitLabelData"

    wintric_class: str = "is-fs16"
