from typing import Union

import os
from bs4.element import Tag
from datetime import datetime, timedelta
from itertools import product
from tqdm import tqdm

from boatrace.common import get_beautiful_soup
from boatrace.parameter import Grade
from boatrace.parameter import ScheduleUrls
from boatrace.scrape.schedule import ScheduleColumns
from boatrace.scrape.schedule import ScheduleTableInfoInHtml

from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM



class ScheduleScraping:

    def __init__(self):
        self._column = ScheduleColumns()

    def scrape(self, years=Union[int, list[int]], grade_types=Union[Grade, list[Grade]]) -> list[dict]:
        if not isinstance(years, list):
            years = [years]
        if not isinstance(grade_types, list):
            grade_types = [grade_types]

        scrape_datas = []
        iter = product(years, grade_types)
        for year, grade_type in tqdm(iter, total=len(years) * len(grade_types)):
            url = ScheduleUrls.FMT_SCHEDULE.format(year, grade_type.value)
            soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

            # get tr in tbody element
            tbody_soups = soup.find_all("tbody")
            tr_soups = []
            for tbody_soup in tbody_soups:
                tr_soups += tbody_soup.find_all("tr")

            for tr_soup in tr_soups:
                scrape_datas += self._extract_schedule_info(year, tr_soup)

        return scrape_datas

    def _extract_schedule_info(self, year: int, tr_soup: Tag) -> list[dict]:
        td_soups = tr_soup.find_all("td")
        offset_idx = 0 if len(td_soups) >= ScheduleTableInfoInHtml.n_cols else -1

        def get_begin_end_date():
            begin_date, end_date = td_soups[ScheduleTableInfoInHtml.col_date + offset_idx].text.strip().split("-")
            return begin_date, end_date

        def get_place_no():
            place_img_path = td_soups[ScheduleTableInfoInHtml.col_place_img + offset_idx].find("img").get("src")
            place_img_name, _ = os.path.splitext(os.path.basename(place_img_path))
            place_no = place_img_name.replace("text_place1_", "")
            return place_no

        def get_grade():
            grade = td_soups[ScheduleTableInfoInHtml.col_grade + offset_idx].attrs["class"][-1].replace("is-", "")
            return grade

        def get_timezone():
            timezone = "" if ("class" not in td_soups[ScheduleTableInfoInHtml.col_timezone + offset_idx].attrs) else td_soups[4 + offset_idx].attrs["class"][0].replace("is-", "")
            return timezone

        def get_title():
            title = td_soups[ScheduleTableInfoInHtml.col_title + offset_idx].text.strip()
            return title

        def get_is_held():
            is_held = td_soups[ScheduleTableInfoInHtml.col_winner + offset_idx].find("a").text.strip() != ""
            return is_held

        begin_date, end_date = get_begin_end_date()
        place_no = get_place_no()
        grade = get_grade()
        timezone = get_timezone()
        title = get_title()
        is_held = get_is_held()

        curr_datetime = datetime.strptime(f"{year}/{begin_date}", "%Y/%m/%d")
        end_datetime = datetime.strptime(f"{year}/{end_date}", "%Y/%m/%d")

        scrape_datas = []
        while curr_datetime <= end_datetime:
            for rno in range(TOOL_PARAM.race_no_range[0], TOOL_PARAM.race_no_range[1] + 1):
                scrape_datas.append(self._column.cast([
                    rno,
                    place_no,
                    curr_datetime,
                    grade,
                    timezone,
                    title,
                    is_held
                ]))
            curr_datetime += timedelta(days=1)
        return scrape_datas
