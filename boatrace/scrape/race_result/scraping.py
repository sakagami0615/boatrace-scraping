from bs4.element import Tag
from datetime import datetime

from boatrace.common import sanitize_text
from boatrace.common import split_list
from boatrace.common import get_beautiful_soup

from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_result import RaceResultReturnTableInfoInHtml
from boatrace.scrape.race_result import RaceResultTimeIndex
from boatrace.scrape.race_result import RaceResultWeatherIndex
from boatrace.scrape.race_result import RaceResultReturnIndex
from boatrace.scrape.race_result import RaceResultHtmlClass
from boatrace.scrape.race_result import RaceResultColumns
from boatrace.scrape.race_result import RaceReturnColumns
from boatrace.setting import CUSTOM_PARAM


class RaceResultScraping:
    """レース結果のスクレイピング"""

    def __init__(self):
        self._result_columns = RaceResultColumns()
        self._return_columns = RaceReturnColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> tuple[list[dict], list[dict]]:
        url = RaceInfoUrls.FMT_RACE_RESULT.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

        time_soup, start_soup, return_soup, a = soup.find_all("table", class_=RaceResultHtmlClass.result_table_class)
        weather_soup = soup.find("div", class_=RaceResultHtmlClass.weather_table_class)
        restoration_soup = soup.find("table", class_=RaceResultHtmlClass.restoration_div_class)
        wintric_soup = soup.find("table", class_=RaceResultHtmlClass.wintric_div_class)

        time_tbody_soups = time_soup.find_all("tbody")
        return_tbody_soups = return_soup.find_all("tbody")
        start_td_soups = start_soup.find_all("td")

        result_datas, return_datas = [], []
        for time_tbody_soup, start_td_soup in zip(time_tbody_soups, start_td_soups):
            result_datas.append(self._extract_result(race_id, stadium_id, date,
                                                     time_tbody_soup, start_td_soup, weather_soup, restoration_soup, wintric_soup))
        for return_tbody_soup in return_tbody_soups:
            return_data = self._extract_return(race_id, stadium_id, date, return_tbody_soup)
            if return_data:
                return_datas += return_data
        return result_datas, return_datas

    def _extract_result(self, race_id: int, stadium_id: int, date: datetime,
                        time_soup: Tag, start_soup: Tag, weather_soup: Tag, restoration_soup: Tag, wintric_soup: Tag) -> dict:
        time_td_soups = time_soup.find_all("td")
        rank = time_td_soups[RaceResultTimeIndex.rank].text.strip()
        frame = time_td_soups[RaceResultTimeIndex.frame].text.strip()
        racer_id, racer_name = sanitize_text(time_td_soups[RaceResultTimeIndex.racer].text).split()
        racetime = time_td_soups[RaceResultTimeIndex.racetime].text

        start_timing = start_soup.find("span", class_=RaceResultHtmlClass.st_class).text

        weather_unit_soups = weather_soup.find_all("div", class_=RaceResultHtmlClass.weather_bodyunit_class)
        temperature = weather_unit_soups[RaceResultWeatherIndex.temperature].find("span", class_=RaceResultHtmlClass.temperature_class).text
        weather = weather_unit_soups[RaceResultWeatherIndex.weather].find("span", class_=RaceResultHtmlClass.weather_class).text
        wind_velocity = weather_unit_soups[RaceResultWeatherIndex.wind_velocity].find("span", class_=RaceResultHtmlClass.wind_velocity_class).text
        wind_direction = weather_unit_soups[RaceResultWeatherIndex.wind_direction].find("p").attrs["class"][-1]
        water_temperature = weather_unit_soups[RaceResultWeatherIndex.water_temperature].find("span", class_=RaceResultHtmlClass.water_temperature_class).text
        wave_height = weather_unit_soups[RaceResultWeatherIndex.wave_height].find("span", class_=RaceResultHtmlClass.wave_height_class).text

        restoration_span_soups = restoration_soup.find_all("span", RaceResultHtmlClass.restoration_class)
        restoration = ",".join([restoration_span_soup.text.strip() for restoration_span_soup in restoration_span_soups])

        wintric = wintric_soup.find("td", class_=RaceResultHtmlClass.wintric_class).text

        return self._result_columns.cast([
            race_id,
            stadium_id,
            date,
            rank,
            frame,
            racer_id,
            racer_name,
            racetime,
            start_timing,
            temperature,
            weather,
            wind_velocity,
            wind_direction,
            water_temperature,
            wave_height,
            restoration,
            wintric
        ])

    def _extract_return(self, race_id: int, stadium_id: int, date: datetime, return_soup: Tag) -> list[dict]:
        td_soups = return_soup.find_all("td")
        # bet_typeをpopし、テーブル行ごとにデータ分割して組番以下の情報を取得する
        bet_type = td_soups.pop(0).text

        line_td_soups = split_list(td_soups, n_item=RaceResultReturnTableInfoInHtml.n_cols - 1)

        scrape_datas = []
        for td_soups in line_td_soups:
            bet_number = "".join([item.text.strip() for item in td_soups[RaceResultReturnIndex.bet_number].find_all("span")])
            return_money = td_soups[RaceResultReturnIndex.return_money].text
            popularity = td_soups[RaceResultReturnIndex.popularity].text

            if bet_number:
                scrape_datas.append(self._return_columns.cast([
                    race_id,
                    stadium_id,
                    date,
                    bet_type,
                    bet_number,
                    return_money,
                    popularity
                ]))
        return scrape_datas
