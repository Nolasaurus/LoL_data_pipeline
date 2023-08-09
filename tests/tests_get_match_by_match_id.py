import unittest
from unittest.mock import patch
from get_match_by_match_id import get_match_by_match_id

class TestGetMatchByMatchId(unittest.TestCase):

    @patch('get_match_by_match_id.requests.get')
    def test_successful_case(self, mock_get):
        # Mocking a successful response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'match_key': 'match_value'} # Example match data

        match_id = 'valid_match_id'
        result = get_match_by_match_id(match_id)

        self.assertEqual(result, {'match_key': 'match_value'})

    @patch('get_match_by_match_id.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        match_id = 'invalid_match_id'
        result = get_match_by_match_id(match_id)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
