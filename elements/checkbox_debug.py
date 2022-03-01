"""
    Get Debug Checkbox Element
"""

import PySimpleGUI as sg


def get_debug_checkbox_element():
    """
    Get Title Element
    :return: List
    """

    return [
        sg.Push(),
        sg.Checkbox('Debug', key='-CHECK DEBUG-', enable_events=True),
    ]
