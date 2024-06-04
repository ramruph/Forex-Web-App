import unittest
import os
import sys
from unittest.mock import patch
import json

# Ensure the src directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from oanda_api import OandaAPI

class TestIntegration(unittest.TestCase):
    @patch('oanda_api.requests.get')
    def test_fetch_instruments(self, mock_get):
        mock_response = {
            "instruments": [
                {"name": "EUR_USD", "type": "CURRENCY", "displayName": "EUR/USD", "pipLocation": -4, "marginRate": "0.02"},
                {"name": "GBP_USD", "type": "CURRENCY", "displayName": "GBP/USD", "pipLocation": -4, "marginRate": "0.02"}
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        api = OandaAPI()
        code, data = api.fetch_instruments()
        self.assertEqual(code, 200)
        self.assertEqual(data, mock_response)

    @patch('oanda_api.requests.get')
    def test_fetch_candles(self, mock_get):
        mock_response = {
            "candles": [
                {
                    "time": "2023-01-01T00:00:00Z",
                    "mid": {"o": "1.1", "h": "1.2", "l": "1.05", "c": "1.15"},
                    "volume": 1000,
                    "complete": True
                },
                {
                    "time": "2023-01-01T00:01:00Z",
                    "mid": {"o": "1.2", "h": "1.25", "l": "1.1", "c": "1.18"},
                    "volume": 1500,
                    "complete": True
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        api = OandaAPI()
        code, df = api.fetch_candles('GBP_USD', 'M1')
        self.assertEqual(code, 200)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['mid_o'], 1.1)
        self.assertEqual(df.iloc[1]['mid_o'], 1.2)

if __name__ == '__main__':
    unittest.main()
