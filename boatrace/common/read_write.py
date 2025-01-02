from typing import Any

import toml
import pickle


def read_toml(toml_filepath: str) -> dict:
    """tomlファイルの読み込み"""
    with open(toml_filepath) as f:
        obj = toml.load(f)
    return obj


def read_pickle(pickle_filepath: str) -> Any:
    """pickleファイルの読み込み"""
    with open(pickle_filepath, mode="rb") as f:
        obj = pickle.load(f)
    return obj

def write_pickle(pickle_filepath: str, data: Any) -> None:
    """pickleファイルの書き込み"""
    with open(pickle_filepath, mode="wb") as f:
        pickle.dump(data, f)
