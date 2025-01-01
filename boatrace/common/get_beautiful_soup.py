from typing import Union

import os
import requests
from bs4 import BeautifulSoup
from time import sleep

from boatrace.common import read_pickle, write_pickle



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
    return os.path.join(cache_dirpath, f"{dirname}-{basename}.pickle")


def get_beautiful_soup(url: str, cache_dirpath=None) -> BeautifulSoup:
    cache_html_path = _get_html_cache_path(url, cache_dirpath)
    if cache_html_path and os.path.isfile(cache_html_path):
        return BeautifulSoup(read_pickle(cache_html_path), 'html.parser')

    response = requests.get(url)
    sleep(2)

    _create_html_cache(cache_html_path, response.text)
    return BeautifulSoup(response.text, "html.parser")
