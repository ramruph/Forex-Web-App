import unittest
import os
import sys

# Ensure the src directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_kpi_data(self):
        response = self.app.get('/kpi_data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

    def test_get_price_data(self):
        response = self.app.get('/price_data/GBP_USD')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

if __name__ == '__main__':
    unittest.main()
