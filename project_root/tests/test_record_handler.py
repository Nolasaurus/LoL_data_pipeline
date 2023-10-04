import unittest
from unittest.mock import patch, Mock
from src.record_handler import RecordHandler
import json

class TestRecordHandler(unittest.TestCase):

    def setUp(self):
        self.record_handler = RecordHandler()

    @patch('src.connect_db.connect_db')
    @patch.object(RecordHandler, '_connect_to_db')
    @patch('src.api_client.API_client.get_puuid_by_name')
    def test_check_db_for_summoner_name(self, mock_get_puuid_by_name, mock_connect, mock_db):
        mock_cursor = mock_db.cursor.return_value

        valid_name = "The Steina"
        valid_puuid = "aWzZ7KxMV8LGxgdrCOYQ4Mc8WXoVcH0l6QxLxUkiFNfP98derWmOax6lMGyU7mONopTrx13jm0qU0A"

        # Scenario 1: Summoner name is in the database
        mock_cursor.fetchone.return_value = (valid_name, "")
        result = self.record_handler.check_db_for_summoner_name(valid_name)
        self.assertEqual(result, valid_puuid)

        # Scenario 2: Summoner name is not in the database
        mock_cursor.fetchone.return_value = None
        mock_get_puuid_by_name.return_value = valid_puuid
        result = self.record_handler.check_db_for_summoner_name(valid_name)
        self.assertEqual(result, valid_puuid)


    @patch('src.connect_db.connect_db')
    @patch.object(RecordHandler, '_connect_to_db')
    def test_check_db_for_match_ids(self, mock_connect, mock_db):
        valid_match_ids_list = [
                                "NA1_4751224234",
                                "NA1_4751206163",
                                "NA1_4751194111",
                                "NA1_4751037438",
                                "NA1_4751004634",
                                "NA1_4750986988",
                                "NA1_4750960504",
                                "NA1_4750779469",
                                "NA1_4750767348",
                                "NA1_4750752625",
                                "NA1_4750742205",
                                "NA1_4750733045",
                                "NA1_4750592902",
                                "NA1_4750572642",
                                "NA1_4750536588",
                                "NA1_4750527533",
                                "NA1_4750519159",
                                "NA1_4750055753",
                                "NA1_4750003088",
                                "NA1_4749192309"
                                ]
        
        valid_puuid = "aWzZ7KxMV8LGxgdrCOYQ4Mc8WXoVcH0l6QxLxUkiFNfP98derWmOax6lMGyU7mONopTrx13jm0qU0A"

        mock_cursor = mock_db.cursor.return_value
        mock_cursor.fetchall.return_value = valid_match_ids_list
        result = self.record_handler.check_db_for_match_ids(valid_puuid)
        self.assertEqual(result, valid_match_ids_list)

    @patch('src.connect_db.connect_db')
    @patch.object(RecordHandler, '_connect_to_db')
    @patch('src.api_client.API_client.get_match_by_match_id')
    @patch('src.api_client.API_client.get_match_timeline')
    def test_check_db_for_match(self, mock_get_match_timeline, mock_get_match_by_match_id, mock_connect, mock_db):
        test_match_id = 'NA1_3720451304'
        
        # Load the mock data from files
        with open(f'/home/nolan/projects/LoL_data_pipeline/API_data/match_timelines/{test_match_id}.json', 'r') as file:
            valid_timeline_json = json.load(file)
        with open(f'/home/nolan/projects/LoL_data_pipeline/API_data/matches/{test_match_id}.json', 'r') as file:
            valid_match_json = json.load(file)
        
        mock_get_match_by_match_id.return_value = valid_match_json
        mock_get_match_timeline.return_value = valid_timeline_json

        # Mock the cursor and fetchone methods
        mock_cursor = mock_db.cursor.return_value
        
        # Scenario 1: Match ID is in the database
        mock_cursor.fetchone.return_value = (valid_match_json, valid_timeline_json)
        result = self.record_handler.check_db_for_match(test_match_id)
        self.assertEqual(result, (valid_match_json, valid_timeline_json))

        # Scenario 2: Match ID is not in the database
        mock_cursor.fetchone.return_value = None
        result = self.record_handler.check_db_for_match(test_match_id)
        self.assertEqual(result, (valid_match_json, valid_timeline_json))



if __name__ == '__main__':
    unittest.main()
