"""
    Get Save Path Module
"""

# Standard Library Imports
import os
from uuid import uuid4

# Third Party Imports
import PySimpleGUI as sg

# Local Application Imports
from utils.config_logger import log


def get_save_path():
    """
    Get Save Path
    :return: String
    """

    try:
        chosen_dir = sg.PopupGetFolder('', no_window=True)

        if chosen_dir:
            f_name = '{}.snappy.parquet'.format(uuid4())

            save_path = os.path.join(chosen_dir, f_name)
        else:
            return

        log().info('Save Path Captured')
    except Exception as e:
        log().warning('Exception Caught In get_save_path - {}'.format(e))
        return

    return save_path
