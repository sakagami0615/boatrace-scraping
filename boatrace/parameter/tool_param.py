
from dataclasses import dataclass, field


@dataclass
class ToolParam:
    race_no_range: list[int] = field(default_factory=lambda: [1, 12])
    n_max_day: int = 7
    n_racer: int = 6
