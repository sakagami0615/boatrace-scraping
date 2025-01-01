from typing import Any, Union


def _n_div_split_list(src_list: list[Any], n_div: int) -> list[Any]:
    n = len(src_list)
    if n % n_div:
        raise ValueError("array split does not result in an equal division")

    dst_list = [[] for _ in range(n_div)]
    w = n // n_div
    for idx, src in enumerate(src_list):
        dst_list[idx // w].append(src)
    return dst_list


def _n_item_split_list(src_list: list[Any], n_item: int) -> list[Any]:
    n = len(src_list)
    if n % n_item:
        raise ValueError("array split does not result in an equal division")

    l = n // n_item
    dst_list = [[] for _ in range(l)]
    for idx, src in enumerate(src_list):
        dst_list[idx // n_item].append(src)
    return dst_list


def split_list(src_list: list[Any], n_div: Union[int, None]=None, n_item: Union[int, None]=None) -> list[Any]:
    if n_div:
        return _n_div_split_list(src_list, n_div)
    elif n_item:
        return _n_item_split_list(src_list, n_item)
    else:
        return src_list

