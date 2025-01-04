from typing import Union

import os
import requests
from bs4 import BeautifulSoup
from time import sleep

from boatrace.common import read_pickle, write_pickle
from boatrace.setting import CUSTOM_LOGGER


logger = CUSTOM_LOGGER.create_logger(__name__)


def _create_html_cache(html_path: Union[str, None], html_text: str) -> None:
    if html_path is None:
        return
    os.makedirs(os.path.dirname(html_path) , exist_ok=True)
    write_pickle(html_path, html_text)


def _get_html_cache_path(url: str, cache_dirpath=None):
    if cache_dirpath is None:
        return None
    basename = os.path.basename(url)
    dirname = os.path.basename(os.path.dirname(url))

    # windowsではファイル名に?を使用できないので、全角に変換
    basename = basename.replace("?", "？")

    return os.path.join(cache_dirpath, f"{dirname}-{basename}.pickle")


def get_beautiful_soup(url: str, cache_dirpath=None, sleep_time: int = 2) -> BeautifulSoup:
    """HTMLのパースデータを取得
    (キャッシュフォルダを指定した場合、取得したHTML情報をキャッシュフォルダに保存)

    Args:
        url (str): 取得先URL
        cache_dirpath (_type_, optional): キャッシュフォルダパス (Defaults to None.)
        sleep_time (int): HTML取得後の待機時間 (Defaults to 2.)

    Returns:
        BeautifulSoup: HTMLパースデータ
    """
    cache_html_path = _get_html_cache_path(url, cache_dirpath)
    if cache_html_path and os.path.isfile(cache_html_path):
        logger.info(f"Get URL request in cache ({url})")
        return BeautifulSoup(read_pickle(cache_html_path), 'html.parser')

    logger.info(f"Get URL request ({url})")
    response = requests.get(url)
    sleep(sleep_time)

    _create_html_cache(cache_html_path, response.text)
    return BeautifulSoup(response.text, "html.parser")
