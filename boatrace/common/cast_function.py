from typing import Any
from datetime import datetime

from boatrace.common import sanitize_text


def Datetime(value: Any) -> datetime:
    """時刻データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "2024/12/24")

    Returns:
        datetime: 時刻データ
    """
    if isinstance(value, datetime):
        return value
    else:
        return datetime.strptime(value, "%Y/%m/%d")


def Set(value: Any) -> set:
    """集合データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "A,B,C")

    Returns:
        set: 集合データ
    """
    if isinstance(value, str):
        return set([sanitize_text(d) for d in value.split(",")])
    else:
        return set(value)


def List(value: Any) -> list:
    """配列データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "A,B,C")

    Returns:
        list: 配列データ
    """
    if isinstance(value, str):
        return [sanitize_text(d) for d in value.split(",")]
    else:
        return list(value)


def Name(value: Any) -> str:
    """名前データへのキャスト関数
    (苗字と名前の間の空白は削除する)

    Args:
        value (Any): 変換前データ(ex: "山田 太郎")

    Returns:
        str: 名前文字列
    """
    return sanitize_text(str(value).replace("　", "").replace(" ", ""))


def Age(value: Any) -> int:
    """年齢データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "10歳")

    Returns:
        int: 年齢データ
    """
    if isinstance(value, str):
        return int(sanitize_text(value.replace("歳", "")))
    else:
        return int(value)


def Weight(value: Any) -> float:
    """重量データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "50kg")

    Returns:
        float: 体重データ
    """
    if isinstance(value, str):
        return float(sanitize_text(value.replace("kg", "")))
    else:
        return float(value)


def Temperature(value: Any) -> float:
    """温度データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "30℃")

    Returns:
        float: 温度データ
    """
    if isinstance(value, str):
        return float(sanitize_text(value.replace("℃", "")))
    else:
        return float(value)


def Distance(value: Any) -> float:
    """距離データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex1: "50cm", ex2: "50m")

    Returns:
        float: 距離データ
    """
    if isinstance(value, str):
        return float(sanitize_text(value.replace("cm", "").replace("m", "")))
    else:
        return float(value)


def StartTiming(value: Any) -> float:
    """スタートタイミングデータへのキャスト関数
    (決まり手の文字があった場合は、削除する)

    Args:
        value (Any): 変換前データ(ex1: ".1", ex1: "F.1")

    Returns:
        float: スタートタイミングデータ
    """
    if isinstance(value, str):
        # 改行文字で分割し、「決まり手」の文字を分ける
        tokens = sanitize_text(value.replace("F", "-")).split()
        return float(tokens[0])
    else:
        return float(value)


def Money(value: Any) -> int:
    """金額データへのキャスト関数

    Args:
        value (Any): 変換前データ(ex: "¥1,000")

    Returns:
        int: 金額データ
    """
    if isinstance(value, str):
        return int(sanitize_text(value.replace("¥", "").replace(",", "")))
    else:
        return int(value)
