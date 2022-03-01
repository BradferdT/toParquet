"""
    Main
"""

import PySimpleGUI as sg
import pandas as pd
import pyarrow

from actions.get_save_path import get_save_path
from actions.prepare_data import prepare_data
from utils.config_logger import configure_logging, log
from views.app import get_app

from utils.get_app_path import get_app_path


def main():
    """
    Main
    """

    window = get_app()

    configure_logging(window)
    log().info('JSON To Parquet App Started')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Generate':
            log().info('Generate Action Called')

            data = prepare_data(values['-INPUT-'])

            if data:
                df = pd.DataFrame(data)

                save_path = get_save_path()
            else:
                log().warning('Generate Action Called With No Input')
                continue

            if save_path:
                log().info('Saving Parquet To {}'.format(save_path))
                df.to_parquet(save_path)
            else:
                log().warning('No Save Path Chosen')
                continue

        if event == '-CHECK DEBUG-':
            window['-SEC1-'].update(visible=values['-CHECK DEBUG-'])
            window['-OUTPUT-'].update(visible=values['-CHECK DEBUG-'])


if __name__ == '__main__':
    main()
