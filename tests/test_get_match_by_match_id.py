import unittest
from unittest.mock import patch
import json
from src.api_client import API_client # Assuming the refactored class is saved in api_client.py

class TestGetMatchByMatchId(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_successful_case(self, mock_get):
        # Read the expected response from the JSON file
        with open('tests/files/NA1_4729149632_match_data.json', 'r') as file:
            expected_match_data = json.load(file)

        # Mocking a successful response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected_match_data

        match_id = 'NA1_4729149632'
        client = API_client()
        result = client.get_match_by_match_id(match_id)

        self.assertEqual(result, expected_match_data)

    @patch('src.api_client.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        match_id = 'invalid_match_id'
        client = API_client()
        result = client.get_match_by_match_id(match_id)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
