from dataclasses import dataclass

from boatrace.common import read_toml


@dataclass
class CustomParam:
    save_html_cache: bool = False
    cache_folder: str = "./cache"


def create_custom_param(toml_filepath: str = "./pyproject.toml") -> CustomParam:
    """tomlファイルからユーザ指定パラメータの読み込み"""

    obj = read_toml(toml_filepath)
    if "tool" in obj and "boatrace" in obj["tool"]:
        return CustomParam(**obj["tool"]["boatrace"])
    else:
        return CustomParam()
