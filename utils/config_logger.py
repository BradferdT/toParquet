"""
    Configure Logging Module
"""

import logging


LOGGER_NAME = 'TO_PARQUET'


def configure_logging(w):
    """
    Configure Logging Class
    :param w: Class
    :return: Void
    """

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)

    log_format = '%(asctime)s - %(levelname)s: %(message)s'
    formatter = logging.Formatter(log_format)

    view_handler = logging.StreamHandler(w['-OUTPUT-'])
    view_handler.setFormatter(formatter)

    logger.addHandler(view_handler)


def log():
    """
    Get Logger
    :return:
    """

    return logging.getLogger(LOGGER_NAME)
