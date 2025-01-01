from typing import Any
from datetime import datetime


def Datetime(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value
    else:
        return datetime.strptime(value, "%Y/%m/%d")


def Set(value: Any) -> set:
    if isinstance(value, str):
        return set([d.strip() for d in value.split(",")])
    else:
        return set(value)


def List(value: Any) -> list:
    if isinstance(value, str):
        return [d.strip() for d in value.split(",")]
    else:
        return list(value)


def Name(value: Any) -> str:
    return str(value).replace("　", "").replace(" ", "").strip()


def Age(value: Any) -> int:
    if isinstance(value, str):
        return int(value.replace("歳", "").strip())
    else:
        return int(value)


def Weight(value: Any) -> float:
    if isinstance(value, str):
        return float(value.replace("kg", "").strip())
    else:
        return float(value)


def Temperature(value: Any) -> float:
    if isinstance(value, str):
        return float(value.replace("℃", "").strip())
    else:
        return float(value)


def Distance(value: Any) -> float:
    if isinstance(value, str):
        return float(value.replace("cm", "").replace("m", "").strip())
    else:
        return float(value)


def StartTiming(value: Any) -> float:
    if isinstance(value, str):
        return float(value.replace("F", "-").strip())
    else:
        return float(value)


def Money(value: Any) -> int:
    if isinstance(value, str):
        return int(value.replace("¥", "").replace(",", "").strip())
    else:
        return int(value)
