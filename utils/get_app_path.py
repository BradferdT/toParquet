"""
    Get Application Path
"""

# Standard Library Imports
import os, sys


def get_app_path():
    """
    Gets Current Application Path

    :return: String
    """

    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    else:
        application_path = os.getcwd()

    return application_path
