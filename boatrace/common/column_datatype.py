from typing import Any, Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class ColumnDatatype:
    """カラムの名前とデータ型を管理するクラス"""
    name: str
    datatype: Callable

    def cast(self, value: Any) -> Any:
        """入力値のデータ型変換
        (変換に失敗した場合は、np.nanを返却)
        """
        if value is None:
            return np.nan
        try:
            if isinstance(value, str):
                value = value.strip()
            return self.datatype(value)
        except ValueError:
            return np.nan
