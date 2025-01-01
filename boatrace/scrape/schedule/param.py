from dataclasses import dataclass

@dataclass
class ScheduleTableInfoInHtml:
    n_cols:         int = 8
    col_date:       int = 1
    col_place_img:  int = 2
    col_grade:      int = 3
    col_timezone:   int = 4
    col_title:      int = 5
    col_winner:     int = 6
