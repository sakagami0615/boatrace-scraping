from typing import Any
from boatrace.common import ColumnDatatype


class ColumnsMixin:
    @property
    def n_columns(self) -> int:
        return len(self.__dict__.values())

    def get_fields(self) -> list[ColumnDatatype]:
        return list(self.__dict__.values())

    def cast(self, datas: list[Any]) -> dict:
        col_infos = self.get_fields()
        return {col_info.name: col_info.cast(data) for col_info, data in zip(col_infos, datas)}
