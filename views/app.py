"""
    Module For Getting View
"""

# Standard Library Imports
import os

# Third Party Imports
import PySimpleGUI as sg

# Local Application Imports
from elements.checkbox_debug import get_debug_checkbox_element
from elements.multiline_debug import get_debug_multiline_element
from elements.button_generate import get_generate_button_element
from elements.multiline_json_input import get_json_input_multiline_element
from elements.title import get_title_element

from utils.get_app_path import get_app_path


def get_app():
    """
    Get MultiLine View

    :return: List
    """

    layout = [
        get_title_element(),
        get_json_input_multiline_element(),
        get_generate_button_element(),
        get_debug_checkbox_element(),
        get_debug_multiline_element(),
    ]

    icon_dir = os.path.join(get_app_path(), 'public', 'bread.ico')

    return sg.Window(
        'JSON To Parquet', layout, icon=icon_dir, font='courier'
    ).Finalize()
