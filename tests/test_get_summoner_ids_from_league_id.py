import unittest
from unittest.mock import patch
from src.get_summoner_ids_from_league_id import get_summoner_ids_from_league_id

class TestGetSummonerIdsFromLeagueId(unittest.TestCase):

    @patch('src.get_summoner_ids_from_league_id.requests.get')
    def test_successful_case(self, mock_get):
        # Reading the expected summoner IDs from the file
        with open('tests/files/summoner_ids_from_league_id', 'r') as file:
            summoner_ids = [line.strip() for line in file]

        # Create the expected JSON response from the API
        expected_data = {
            'entries': [{'summonerId': summoner_id} for summoner_id in summoner_ids]
        }

        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data

        league_id = '0003dc0a-d06f-4a0f-872f-bfcc4f526f9'
        result = get_summoner_ids_from_league_id(league_id)

        self.assertEqual(result, summoner_ids)

    @patch('src.get_summoner_ids_from_league_id.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        league_id = 'invalid_league_id'
        result = get_summoner_ids_from_league_id(league_id)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
