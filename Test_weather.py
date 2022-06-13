import unittest
from unittest.mock import patch, MagicMock

from Ivashchenko_HW_15 import weather_output


class GettingWeatherTest(unittest.TestCase):

    @patch('getting_weather.requests')
    def test_error_from_server(self, requests_mock):
        request_response_mock = MagicMock()
        request_response_mock.status_code = 404
        request_response_mock.json.return_value = {'message': "City not found"}
        requests_mock.get.return_value = request_response_mock

        with self.assertRaises(RuntimeError):
            weather_output('Kharkov')
