from typing import Union

import os
import logging
from logging import FileHandler, Formatter, StreamHandler, getLogger


class CustomLogger:
    """ロガークラス"""
    top_name: Union[str, None] = None
    save_log_path: Union[str, None] = None

    def __init__(self, save_log_path: Union[str, None] = None):
        if self.save_log_path is None:
            self.save_log_path = save_log_path

    def _get_formatter(self) -> Formatter:
        return Formatter("[%(asctime)s] [%(levelname)s] " "[%(filename)s:%(lineno)d - %(funcName)s] %(message)s")

    def _set_save_logger(self, logger: logging.Logger):
        if self.save_log_path is None:
            return

        os.makedirs(os.path.dirname(self.save_log_path), exist_ok=True)
        file_handler = FileHandler(filename=self.save_log_path, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self._get_formatter())
        logger.addHandler(file_handler)

    def create_logger(self, name: str):
        if CustomLogger.top_name is None:
            CustomLogger.top_name = name
            logger = getLogger(CustomLogger.top_name)
            logger.setLevel(logging.INFO)

            stream_handler = StreamHandler()
            stream_handler.setFormatter(self._get_formatter())
            stream_handler.setLevel(logging.WARNING)
            logger.addHandler(stream_handler)

            self._set_save_logger(logger)
            return logger
        else:
            logger = getLogger(CustomLogger.top_name).getChild(name)
            return logger
