from bs4.element import Tag
from datetime import datetime

from boatrace.common import get_beautiful_soup

from boatrace.parameter import RaceInfoUrls
from boatrace.scrape.race_before import RaceBeforeRacerStatusIndex
from boatrace.scrape.race_before import RaceBeforeWeatherIndex
from boatrace.scrape.race_before import RaceBeforeHtmlClass
from boatrace.scrape.race_before import RaceBeforeColumns
from boatrace.setting import CUSTOM_PARAM, TOOL_PARAM


class RaceBeforeScraping:
    """事前情報のスクレイピング"""

    def __init__(self):
        self._column = RaceBeforeColumns()

    def scrape(self, race_id: int, stadium_id: int, date: datetime) -> list[dict]:
        url = RaceInfoUrls.FMT_BEFORE_INFO.format(race_id, stadium_id, date)
        soup = get_beautiful_soup(url, CUSTOM_PARAM.cache_folder)

        racer_soup = soup.find("table", class_=RaceBeforeHtmlClass.racer_table_class)
        start_soup = soup.find("table", class_=RaceBeforeHtmlClass.start_table_class)
        weather_soup = soup.find("div", class_=RaceBeforeHtmlClass.weather_div_class)

        racer_tbody_soups = racer_soup.find_all("tbody")
        start_tr_soups = start_soup.find("tbody").find_all("tr")

        # 出場と欠場の選手でtbodyを分割
        valid_racer_tbody_soups, invalid_racer_tbody_soups = [], []
        for racer_tbody_soup in racer_tbody_soups:
            if RaceBeforeHtmlClass.absent_tbody_class not in racer_tbody_soup["class"]:
                valid_racer_tbody_soups.append(racer_tbody_soup)
            else:
                invalid_racer_tbody_soups.append(racer_tbody_soup)

        scrape_datas = []
        # 出場選手の情報をappend
        for racer_tbody_soup, start_tr_soup in zip(valid_racer_tbody_soups, start_tr_soups):
            scrape_datas.append(self._extract_valid_race_before(race_id, stadium_id, date, racer_tbody_soup, start_tr_soup, weather_soup))
        # 出場欠場の情報をappend
        for racer_tbody_soup in invalid_racer_tbody_soups:
            scrape_datas.append(self._extract_invalid_race_before(race_id, stadium_id, date, racer_tbody_soup, weather_soup))
        return scrape_datas

    def _extract_valid_race_before(self, race_id: int, stadium_id: int, date: datetime, racer_soup: Tag, start_soup: Tag, weather_soup: Tag) -> dict:
        """出場選手のデータを取得"""
        racer_td_soups = racer_soup.find_all("td")
        frame = racer_td_soups[RaceBeforeRacerStatusIndex.frame].text
        name = racer_td_soups[RaceBeforeRacerStatusIndex.name].text
        weight = racer_td_soups[RaceBeforeRacerStatusIndex.weight].text
        adjust_weight = racer_td_soups[RaceBeforeRacerStatusIndex.adjust_weight].text
        exhibit_time = racer_td_soups[RaceBeforeRacerStatusIndex.exhibit_time].text
        tilt = racer_td_soups[RaceBeforeRacerStatusIndex.tilt].text
        propeller = racer_td_soups[RaceBeforeRacerStatusIndex.propeller].text
        parts_replace = racer_td_soups[RaceBeforeRacerStatusIndex.parts_replace].text
        before_result_r = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_r].text
        before_result_entry = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_entry].text
        before_result_st = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_st].text
        before_result_rank = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_rank].text

        st = start_soup.find("span", class_=RaceBeforeHtmlClass.start_tr_class).text

        weather_unit_soups = weather_soup.find_all("div", class_=RaceBeforeHtmlClass.weather_bodyunit_class)
        temperature = weather_unit_soups[RaceBeforeWeatherIndex.temperature].find("span", class_=RaceBeforeHtmlClass.temperature_class).text
        weather = weather_unit_soups[RaceBeforeWeatherIndex.weather].find("span", class_=RaceBeforeHtmlClass.weather_class).text
        wind_velocity = weather_unit_soups[RaceBeforeWeatherIndex.wind_velocity].find("span", class_=RaceBeforeHtmlClass.wind_velocity_class).text
        wind_direction = weather_unit_soups[RaceBeforeWeatherIndex.wind_direction].find("p").attrs["class"][-1].replace("is-", "")
        water_temperature = weather_unit_soups[RaceBeforeWeatherIndex.water_temperature].find("span", class_=RaceBeforeHtmlClass.water_temperature_class).text
        wave_height = weather_unit_soups[RaceBeforeWeatherIndex.wave_height].find("span", class_=RaceBeforeHtmlClass.wave_height_class).text

        return self._column.cast([
            race_id,
            stadium_id,
            date,
            frame,
            name,
            weight,
            adjust_weight,
            exhibit_time,
            tilt,
            propeller,
            parts_replace,
            before_result_r,
            before_result_entry,
            before_result_st,
            before_result_rank,
            st,
            temperature,
            weather,
            wind_velocity,
            wind_direction,
            water_temperature,
            wave_height,
        ])

    def _extract_invalid_race_before(self, race_id: int, stadium_id: int, date: datetime, racer_soup: Tag, weather_soup: Tag) -> dict:
        """欠場選手のデータを取得"""
        racer_td_soups = racer_soup.find_all("td")
        frame = None
        name = racer_td_soups[RaceBeforeRacerStatusIndex.name].text
        weight = racer_td_soups[RaceBeforeRacerStatusIndex.weight].text
        adjust_weight = racer_td_soups[RaceBeforeRacerStatusIndex.adjust_weight].text
        exhibit_time = racer_td_soups[RaceBeforeRacerStatusIndex.exhibit_time].text
        tilt = racer_td_soups[RaceBeforeRacerStatusIndex.tilt].text
        propeller = racer_td_soups[RaceBeforeRacerStatusIndex.propeller].text
        parts_replace = racer_td_soups[RaceBeforeRacerStatusIndex.parts_replace].text
        before_result_r = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_r].text
        before_result_entry = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_entry].text
        before_result_st = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_st].text
        before_result_rank = racer_td_soups[RaceBeforeRacerStatusIndex.before_result_rank].text

        st = None

        weather_unit_soups = weather_soup.find_all("div", class_=RaceBeforeHtmlClass.weather_bodyunit_class)
        temperature = weather_unit_soups[RaceBeforeWeatherIndex.temperature].find("span", class_=RaceBeforeHtmlClass.temperature_class).text
        weather = weather_unit_soups[RaceBeforeWeatherIndex.weather].find("span", class_=RaceBeforeHtmlClass.weather_class).text
        wind_velocity = weather_unit_soups[RaceBeforeWeatherIndex.wind_velocity].find("span", class_=RaceBeforeHtmlClass.wind_velocity_class).text
        wind_direction = weather_unit_soups[RaceBeforeWeatherIndex.wind_direction].find("p").attrs["class"][-1].replace("is-", "")
        water_temperature = weather_unit_soups[RaceBeforeWeatherIndex.water_temperature].find("span", class_=RaceBeforeHtmlClass.water_temperature_class).text
        wave_height = weather_unit_soups[RaceBeforeWeatherIndex.wave_height].find("span", class_=RaceBeforeHtmlClass.wave_height_class).text

        return self._column.cast([
            race_id,
            stadium_id,
            date,
            frame,
            name,
            weight,
            adjust_weight,
            exhibit_time,
            tilt,
            propeller,
            parts_replace,
            before_result_r,
            before_result_entry,
            before_result_st,
            before_result_rank,
            st,
            temperature,
            weather,
            wind_velocity,
            wind_direction,
            water_temperature,
            wave_height,
        ])
