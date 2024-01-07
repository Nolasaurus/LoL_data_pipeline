from extract_data import get_champion_stats, get_bans, get_teams
from match_classes import MatchDto, MatchTimelineDto
from unittest import TestCase
import pytest
import json

match_timeline_data_filepath = '/home/nolan/projects/LoL_data_pipeline/tests/files/NA1_4729149632_match_timeline.json'
match_data_filepath = '/home/nolan/projects/LoL_data_pipeline/tests/files/NA1_4729149632_match_data.json'

# Load JSON data and create DTOs
with open(match_data_filepath, 'r') as file:
    match_json = json.load(file)

with open(match_timeline_data_filepath, 'r') as file:
    match_timeline_json = json.load(file)


class TestGetChampionStats(TestCase):
    def test_get_champion_stats(self):
        # Assuming match_timeline_dto is already created from the test data
        actual_values_list = get_champion_stats(match_timeline_json)

        def extract_values_by_frame_and_participant(values_list, target_frame_number, target_participant_id):
            extracted_values = []
            for values_dict in values_list:
                if values_dict["frame_number"] == target_frame_number and values_dict["participant_id"] == target_participant_id:
                    return values_dict  # Return the matching dictionary

            # Return an empty dictionary when no match is found
            return {}

        frame_number_to_extract = 1  # Replace with the desired frame number
        participant_id_to_extract = 1  # Replace with the desired participant ID

        sample_stats = extract_values_by_frame_and_participant(actual_values_list, frame_number_to_extract, participant_id_to_extract)
        self.assertNotEqual(sample_stats, {})
        # Check the length of the result
        expected_length = len(match_timeline_json.info.frames) * len(match_timeline_json.info.frames[0].participant_frames)
        self.assertEqual(len(actual_values_list), expected_length)

        self.assertEqual(sample_stats['armor'], 0)
        self.assertEqual(sample_stats['armor_pen'], 0)
        self.assertEqual(sample_stats['armorPenPercent'], 0.0)
        self.assertEqual(sample_stats['attackDamage'], 68)
        self.assertEqual(sample_stats['attackSpeed'], 167)
        self.assertEqual(sample_stats['bonusArmorPenPercent'], 0.0)
        self.assertEqual(sample_stats['bonusMagicPenPercent'], 0.0)
        self.assertEqual(sample_stats['ccReduction'], 0)
        self.assertEqual(sample_stats['cooldownReduction'], 0)
        self.assertEqual(sample_stats['health'], 292)
        self.assertEqual(sample_stats['healthMax'], 834)
        self.assertEqual(sample_stats['healthRegen'], 14)
        self.assertEqual(sample_stats['lifesteal'], 0.0)
        self.assertEqual(sample_stats['magicPen'], 0)
        self.assertEqual(sample_stats['magicPenPercent'], 0.0)
        self.assertEqual(sample_stats['magicResist'], 51)
        self.assertEqual(sample_stats['movementSpeed'], 340)
        self.assertEqual(sample_stats['omnivamp'], 0.0)
        self.assertEqual(sample_stats['physicalVamp'], 0.0)
        self.assertEqual(sample_stats['power'], 0)
        self.assertEqual(sample_stats['powerMax'], 60)
        self.assertEqual(sample_stats['powerRegen'], 0)
        self.assertEqual(sample_stats['spellVamp'], 0.0)


class TestGetBansFunction(TestCase):
    def test_get_bans(self):

        # Expected output
        expected_bans = []

        # Call the function with the mock data
        actual_bans = get_bans(match_json)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_bans, expected_bans)



class TestGetTeams(TestCase):

    def test_get_teams(self):
        # Assuming match_dto is already created from the JSON data
        teams = get_teams(match_json)

        # Assert the basic structure
        self.assertEqual(len(teams), 2)

        # Assertions for team 1
        self.assertEqual(teams[0]['team_id'], 100)
        self.assertEqual(teams[0]['match_id'], "NA1_4729149632")
        self.assertFalse(teams[0]['baron_first'])
        self.assertEqual(teams[0]['baron_kills'], 0)
        self.assertTrue(teams[0]['champion_first'])
        self.assertEqual(teams[0]['champion_kills'], 33)
        self.assertFalse(teams[0]['dragon_first'])
        self.assertEqual(teams[0]['dragon_kills'], 0)
        self.assertFalse(teams[0]['inhibitor_first'])
        self.assertEqual(teams[0]['inhibitor_kills'], 0)
        self.assertFalse(teams[0]['rift_herald_first'])
        self.assertEqual(teams[0]['rift_herald_kills'], 0)
        self.assertFalse(teams[0]['tower_first'])
        self.assertEqual(teams[0]['tower_kills'], 1)
        self.assertFalse(teams[0]['win'])

        # Assertions for team 2
        self.assertEqual(teams[1]['team_id'], 200)
        self.assertEqual(teams[1]['match_id'], "NA1_4729149632")
        self.assertFalse(teams[1]['baron_first'])
        self.assertEqual(teams[1]['baron_kills'], 0)
        self.assertFalse(teams[1]['champion_first'])
        self.assertEqual(teams[1]['champion_kills'], 76)
        self.assertFalse(teams[1]['dragon_first'])
        self.assertEqual(teams[1]['dragon_kills'], 0)
        self.assertTrue(teams[1]['inhibitor_first'])
        self.assertEqual(teams[1]['inhibitor_kills'], 1)
        self.assertFalse(teams[1]['rift_herald_first'])
        self.assertEqual(teams[1]['rift_herald_kills'], 0)
        self.assertTrue(teams[1]['tower_first'])
        self.assertEqual(teams[1]['tower_kills'], 4)
        self.assertTrue(teams[1]['win'])


