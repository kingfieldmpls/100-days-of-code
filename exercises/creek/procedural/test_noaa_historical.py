<<<<<<< HEAD
import pytest

import noaa_historical as nh

from datetime import datetime, timedelta
from time import strftime
from unittest.mock import Mock, patch

# Run using the last week so we don't need
# to reference variables from the script
start = datetime.today().strftime("%Y-%m-%d")
end = (datetime.today()-timedelta(days=7)).strftime("%Y-%m-%d")


@pytest.fixture()
@patch("noaa_historical.requests.get")
def setup_request_response(mock_get):
    mock_get.return_value.raise_for_status = "ok"
    # I can't figure out how to get a multiline dictionary of dictionaries string to parse correctly
    mock_get.return_value.text = '{"metadata": {"resultset": {"offset": 1, "count": 82, "limit": 250}},"results": [{"date": "2018-09-01T00:00:00", "datatype": "PRCP", "station": "GHCND:USC00214884", "attributes": ",,H,0600", "value": 0.0}, {"date": "2018-09-01T00:00:00", "datatype": "SNOW", "station": "GHCND:USC00214884", "attributes": ",,H,", "value": 0.0}, {"date": "2018-09-01T00:00:00", "datatype": "SNWD", "station": "GHCND:USC00214884", "attributes": ",,H,0600", "value": 0.0}, {"date": "2018-09-01T00:00:00", "datatype": "TMAX", "station": "GHCND:USC00214884", "attributes": ",,H,0600", "value": 83.0}]}'

    data = nh.setup_request(start, end)

    return data


def test_request():
    data = nh.setup_request(start, end)
    assert data is not None


def test_setup_request(setup_request_response):
    data = setup_request_response

    assert data['metadata']['resultset']['count'] == 82
    assert data['metadata']['resultset']['offset'] == 1
    assert data['metadata']['resultset']['limit'] == 250


def test_get_data(setup_request_response):
    data = setup_request_response
    rows = nh.get_data(data)
    assert rows[0] == ['2018-09-01T00:00:00', 'PRCP', 0.0]
    assert rows[1] == ['2018-09-01T00:00:00', 'SNOW', 0.0]
    assert rows[2] == ['2018-09-01T00:00:00', 'SNWD', 0.0]
    assert rows[3] == ['2018-09-01T00:00:00', 'TMAX', 83.0]

# Doing setup a tear down for a database seems a bit next lelvel for where I'm at.
# This is a great resource to view for figuring it out in the future
# https://github.com/pybites/pytip/blob/master/tests/test_tips.py
# Notice the __init__.py in pytip/tips importing functions from db.py
# I think this is what's giving the test access to those functions, but hey
# I still don't really understand __init__.py, but I think when the tips is instantiatied
# You're gaining access to those methods?
=======
import unittest
import noaa_historical


class TestNOAA(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_setupRequest(self):
        result = 
>>>>>>> 8385fc367122e629345e204e651cdf1bed54bbe8
