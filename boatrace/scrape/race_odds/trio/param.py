from dataclasses import dataclass


@dataclass
class OddsTrioTableInfoInHtml:
    n_head_items: int = 18
    n_line_items: int = 12
    line_row_size: int = 4


@dataclass
class OddsTrioHtmlClass:
    tbody_class: str = "is-p3-0"
    td_class: str = "is-fs14"
    disable_class: str = "is-disabled"
