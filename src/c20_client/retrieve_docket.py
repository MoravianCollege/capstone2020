"""
Contains class used to retreive dockets from regulations.gov
"""
import requests
from c20_client.status_code_check import check_status
from c20_client.client_logger import LOGGER


def get_docket_data(api_key, docket_id):
    """
    Makes call to regulations.gov and retrieves the docket data
    """
    LOGGER.info('Requesting docket from regulations.gov')
    response = requests.get("https://api.data.gov:443/" +
                            "regulations/v3/docket.json?api_key=" +
                            api_key +
                            "&docketId=" +
                            docket_id)

    check_status(response.status_code)
    LOGGER.info('docket has been retrieved')

    return response.json()


def get_docket(api_key, docket_id):
    """
    Returns the docket in the format of a JSON file with the current job
    and the data for the current job
    """
    docket = get_docket_data(api_key, docket_id)
    return docket
