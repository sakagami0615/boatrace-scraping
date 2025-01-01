from typing import Any, Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class ColumnDatatype:
    name: str
    datatype: Callable

    def cast(self, value: Any) -> Any:
        if value is None:
            return np.nan
        try:
            if isinstance(value, str):
                value = value.strip()
            return self.datatype(value)
        except ValueError:
            return np.nan
