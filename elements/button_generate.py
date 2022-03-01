"""
    Get Generate Button Element
"""

import PySimpleGUI as sg


def get_generate_button_element():
    """
    Get Title Element
    :return: List
    """

    return [
        sg.Button(
            button_text='Generate',
            size=(15, 2),
            font=('courier', 10),
            auto_size_button=True,
        )
    ]
