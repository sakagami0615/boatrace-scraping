from dataclasses import dataclass


@dataclass
class RaceCardTdIndex:
    frame: int = 0
    racer_status: int = 2
    racer_score: int = 3
    wide: int = 4
    local: int = 5
    motor: int = 6
    boat: int = 7
    result: int = 9


@dataclass
class RaceCardRacerIndex:
    id: int = 0
    cls: int = 1
    name: int = 2
    branch: int = 3
    birthplace: int = 4
    age: int = 5
    weight: int = 6
    fn: int = 7
    ln: int = 8
    avgst: int = 9


@dataclass
class RaceCardWideIndex:
    rate1: int = 0
    rate2: int = 1
    rate3: int = 2


@dataclass
class RaceCardLocalIndex:
    rate1: int = 0
    rate2: int = 1
    rate3: int = 2


@dataclass
class RaceCardMotorIndex:
    no: int = 0
    rate2: int = 1
    rate3: int = 2


@dataclass
class RaceCardBoatIndex:
    no: int = 0
    rate2: int = 1
    rate3: int = 2


@dataclass
class RaceCardHtmlClass:
    table_class: str = "table1 is-tableFixed__3rdadd"
    tbody_class: str = "is-fs12"
