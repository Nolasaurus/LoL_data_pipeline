import unittest
from unittest.mock import patch
import json
from src.get_match_timeline import get_match_timeline

class TestGetMatchTimeline(unittest.TestCase):

    @patch('src.get_match_timeline.requests.get')
    def test_successful_case(self, mock_get):
        # Read the expected response from the JSON file
        with open('tests/files/NA1_4729149632_match_timeline.json', 'r') as file:
            expected_timeline_data = json.load(file)

        # Mocking a successful response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected_timeline_data

        match_id = 'NA1_4729149632'
        result = get_match_timeline(match_id)

        self.assertEqual(result, expected_timeline_data)

    @patch('src.get_match_timeline.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        match_id = 'invalid_match_id'
        result = get_match_timeline(match_id)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
