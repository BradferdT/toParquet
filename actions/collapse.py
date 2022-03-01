"""
    Collapse Module for pinning collapsable elements
"""


# Third Party Imports
import PySimpleGUI as sg


def collapse(layout, key):
    """
    Function that creates a column tha tcan be later made hidden

    :param layout: List
    :param key: String

    :return: Obj
    """

    return sg.pin(sg.Column(layout, key=key))
