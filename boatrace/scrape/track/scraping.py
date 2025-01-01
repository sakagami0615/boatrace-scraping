from tqdm import tqdm

from boatrace.common import get_beautiful_soup
from boatrace.parameter import StadiumUrls
from boatrace.scrape.track import TrackConst
from boatrace.scrape.track import Latest3MonthCourseResultConst
from boatrace.scrape.track import Latest3MonthFrameResultConst
from boatrace.scrape.track import SeasonResultConst
from boatrace.scrape.track import MemoConst
from boatrace.scrape.track import Latest3MonthCourseResultColumns
from boatrace.scrape.track import Latest3MonthFrameResultColumns
from boatrace.scrape.track import SeasonResultColumns
from boatrace.scrape.track import MemoColumns

from boatrace.setting import CUSTOM_PARAM



class TrackScraping:

    def __init__(self):
        self._course_column = Latest3MonthCourseResultColumns()
        self._frame_column = Latest3MonthFrameResultColumns()
        self._season_column = SeasonResultColumns()
        self._memo_column = MemoColumns()

    def scrape(self) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
        course_ids = self._extract_course_ids()

        course_datas, frame_datas, season_datas, memo_datas = [], [], [], []
        for course_id in tqdm(course_ids, total=len(course_ids)):
            course_result, frame_result, season_result, memo_result = self._extract_track_info(course_id)
            course_datas.extend(course_result)
            frame_datas.extend(frame_result)
            season_datas.extend(season_result)
            memo_datas.append(memo_result)
        return course_datas, frame_datas, season_datas, memo_datas

    def _extract_course_ids(self) -> list[str]:
        soup = get_beautiful_soup(StadiumUrls.STADIUM_TOP, CUSTOM_PARAM.cache_folder)
        div_soups = soup.find_all("div", class_=TrackConst.table_class)

        tr_soups = []
        for div_soup in div_soups:
            tr_soups += div_soup.find("tbody").find_all("tr")

        course_ids = []
        for tr_soup in tr_soups:
            course_url = tr_soup.find("a").get("href")
            course_id = course_url.split("=")[-1].strip()
            course_ids.append(course_id)
        return course_ids

    def _extract_track_info(self, course_id: int) -> tuple[list[dict], list[dict], list[dict], dict]:
        url = StadiumUrls.FMT_STADIUM.format(course_id)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

        def get_latest_course_result_data():
            table_soup = soup.find("table", class_=Latest3MonthCourseResultConst.table_class)
            tbody_soups = table_soup.find_all("tbody")
            scrape_datas = []
            for tbody_soup in tbody_soups:
                td_soups = tbody_soup.find("tr").find_all("td")
                datas = [course_id] + [td_soup.text for td_soup in td_soups]
                scrape_datas.append(self._course_column.cast(datas))
            return scrape_datas

        def get_latest_frame_result_data():
            table_soup = soup.find("table", class_=Latest3MonthFrameResultConst.table_class)
            tbody_soups = table_soup.find_all("tbody")
            scrape_datas = []
            for tbody_soup in tbody_soups:
                td_soups = tbody_soup.find("tr").find_all("td")
                datas = [course_id] + [td_soup.text for td_soup in td_soups]
                scrape_datas.append(self._frame_column.cast(datas))
            return scrape_datas

        def get_season_result_data():
            table_soups = soup.find_all("table", class_=SeasonResultConst.table_class)

            spring_tbody_soups = table_soups[0].find_all("tbody")
            summer_tbody_soups = table_soups[1].find_all("tbody")
            autumn_tbody_soups = table_soups[2].find_all("tbody")
            winter_tbody_soups = table_soups[3].find_all("tbody")

            scrape_datas = []
            for spring_tbody_soup, summer_tbody_soup, autumn_tbody_soup, winter_tbody_soup in zip(spring_tbody_soups,
                                                                                                  summer_tbody_soups,
                                                                                                  autumn_tbody_soups,
                                                                                                  winter_tbody_soups):
                spring_td_soups = spring_tbody_soup.find("tr").find_all("td")
                summer_td_soups = summer_tbody_soup.find("tr").find_all("td")
                autumn_td_soups = autumn_tbody_soup.find("tr").find_all("td")
                winter_td_soups = winter_tbody_soup.find("tr").find_all("td")

                # 春季以外の枠は不要なので削除し、extendする
                summer_td_soups.pop(0)
                autumn_td_soups.pop(0)
                winter_td_soups.pop(0)
                season_td_soups = spring_td_soups + summer_td_soups + autumn_td_soups + winter_td_soups
                datas = [course_id] + [td_soup.text for td_soup in season_td_soups]
                scrape_datas.append(self._season_column.cast(datas))
            return scrape_datas

        def get_memo_data():
            frame_soup = soup.find("div", class_=MemoConst.table_class)
            dd_soups = frame_soup.find_all("dd")
            datas = [course_id] + [dd_soup.text for dd_soup in dd_soups]
            return self._memo_column.cast(datas)

        course_result = get_latest_course_result_data()
        frame_result = get_latest_frame_result_data()
        season_result = get_season_result_data()
        memo_result = get_memo_data()
        return course_result, frame_result, season_result, memo_result
