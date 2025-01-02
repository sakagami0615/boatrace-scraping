from typing import Any

from boatrace.common import ColumnDatatype


class ColumnsMixin:
    """カラム定義クラスのMixin"""

    @property
    def n_columns(self) -> int:
        """カラム数を取得"""
        return len(self.__dict__.values())

    def get_fields(self) -> list[ColumnDatatype]:
        """カラム定義クラスのフィールドを取得"""
        return list(self.__dict__.values())

    def cast(self, datas: list[Any]) -> dict:
        """カラム定義に定義したフィールドに従ってキャスト
        (キャストしたデータは辞書に格納して返却)
        """
        col_infos = self.get_fields()
        return {col_info.name: col_info.cast(data) for col_info, data in zip(col_infos, datas)}
