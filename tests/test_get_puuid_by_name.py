import unittest
from unittest.mock import patch
from api_client import API_Client

class TestGetPuuidByName(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @patch('api_client.requests.get')
    def test_successful_case(self, mock_get):
        # Mocking a successful response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'puuid': 'aWzZ7KxMV8LGxgdrCOYQ4Mc8WXoVcH0l6QxLxUkiFNfP98derWmOax6lMGyU7mONopTrx13jm0qU0A'}

        summoner_name = 'The Steina'
        result = API_Client().get_summoner_by_name(summoner_name)

        self.assertEqual(result['puuid'], 'aWzZ7KxMV8LGxgdrCOYQ4Mc8WXoVcH0l6QxLxUkiFNfP98derWmOax6lMGyU7mONopTrx13jm0qU0A')

    @patch('api_client.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        summoner_name = 'InvalidSummonerName'
        result = API_Client().get_summoner_by_name(summoner_name)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()