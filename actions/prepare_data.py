"""
    Prepare Multiline String Input to List of Dicts Module
"""

# Standard Library Imports
from re import findall
from json import loads

from numpy import char

# Local Application Imports
from utils.config_logger import log


def prepare_data(multiline_str):
    """
    Prepare Data

    :param multiline_str: Str
    :return: List
    """

    try:
        log().info('Preparing Data...')

        filter = ''.join([chr(char) for char in range(1, 32)])
        table = str.maketrans('', '', filter)

        multiline_str = multiline_str.strip()
        multiline_str = multiline_str.translate(table)

        matches = findall(r'{.*?}', multiline_str)

        if not matches:
            log().warning('No JSON Objects Found from Provided Input')
            return

        data = [loads(row) for row in matches]
        log().info('JSON Prepared')

    except Exception as e:
        log().error('An Error Occurred While Attempting to Prepare Data: {}'.format(e))
        return

    return data
