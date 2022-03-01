"""
    Multiline Debug Element
"""

# Third Party Imports
import PySimpleGUI as sg
from click import edit

# Local Application Imports
from actions.collapse import collapse


def get_debug_multiline_element():
    """
    Get Title Element
    :return: List
    """

    return [
        sg.Push(),
        collapse(
            [
                [
                    sg.Multiline(
                        key='-OUTPUT-',
                        size=(60, 5),
                        write_only=True,
                        disabled=True,
                        visible=False,
                    )
                ]
            ],
            '-SEC1-',
        ),
        sg.Push(),
    ]
