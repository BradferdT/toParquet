"""
    Get JSON Input Multiline Element
"""

import PySimpleGUI as sg


def get_json_input_multiline_element():
    """
    Get Title Element
    :return: List
    """

    return [
        sg.Multiline(
            key='-INPUT-',
            size=(100, 40),
            font=('courier', 8),
            auto_size_text=True,
        )
    ]
