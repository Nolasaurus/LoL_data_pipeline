import unittest
from unittest.mock import patch
from src.get_match_ids_by_puuid import get_match_ids_by_puuid

class TestGetMatchIdsByPuuid(unittest.TestCase):

    @patch('src.get_match_ids_by_puuid.requests.get')
    def test_successful_case(self, mock_get):
        # Mocking a successful response from the API
        expected_match_ids = [
            "NA1_4656725054",
            "NA1_4656701593",
            "NA1_4644336325"
            ]
            
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = expected_match_ids

        puu_id = 'QeQevDlzR9buXaCEj3GqHyV9ZWxMrs-ltqdgsReyS7_Lu1wuMKhv7xqybkCEbRNHmn2OlqoS_xYjhw'
        result = get_match_ids_by_puuid(puu_id, start=0, count=3)

        self.assertEqual(result, expected_match_ids)

    @patch('src.get_match_ids_by_puuid.requests.get')
    def test_failure_case(self, mock_get):
        # Mocking a failure response from the API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        puu_id = 'invalid_puu_id'
        result = get_match_ids_by_puuid(puu_id)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
