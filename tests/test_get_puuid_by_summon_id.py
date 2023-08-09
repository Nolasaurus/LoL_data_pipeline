import unittest
from unittest.mock import patch
import json
from src.get_puuid_by_summon_id import get_puuid_by_summon_id

class TestGetPuuidBySummonId(unittest.TestCase):

    @patch('src.get_puuid_by_summon_id.requests.get')
    def test_successful_case(self, mock_get):
        # Read the expected response from the JSON file
        with open('tests/files/hNYHxf7iXp1BhGgk_JzZiU00AzmUNQ058d8ZZzKYUYtty87Z.json', 'r') as file:
            expected_data = json.load(file)

        # Mocking a successful response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data

        summoner_id = 'hNYHxf7iXp1BhGgk_JzZiU00AzmUNQ058d8ZZzKYUYtty87Z'
        result = get_puuid_by_summon_id(summoner_id)

        self.assertEqual(result, 'QeQevDlzR9buXaCEj3GqHyV9ZWxMrs-ltqdgsReyS7_Lu1wuMKhv7xqybkCEbRNHmn2OlqoS_xYjhw')

    @patch('src.get_puuid_by_summon_id.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        summoner_id = 'invalid_summoner_id'
        result = get_puuid_by_summon_id(summoner_id)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
