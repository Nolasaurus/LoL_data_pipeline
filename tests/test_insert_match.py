from insert_match import get_champion_stats, get_bans
from match_classes import MatchDto, MatchTimelineDto
from unittest import TestCase
import pytest
import json

match_timeline_data_filepath = '/home/nolan/projects/LoL_data_pipeline/tests/files/NA1_4729149632_match_timeline.json'
match_data_filepath = '/home/nolan/projects/LoL_data_pipeline/tests/files/NA1_4729149632_match_data.json'

# Load JSON data and create DTOs
with open(match_data_filepath, 'r') as file:
    match_data = json.load(file)
match_dto = MatchDto(match_data)

with open(match_timeline_data_filepath, 'r') as file:
    match_timeline_data = json.load(file)
match_timeline_dto = MatchTimelineDto(match_timeline_data)

def test_get_champion_stats():
    # Call the function with the test data
    actual_values_list = get_champion_stats(match_timeline_dto)
    
    # Prepare the expected values list based on the test data
    expected_values_list = get_expected_values(match_timeline_dto)

    # Use TestCase from unittest to assert the lists are equal
    TestCase().assertListEqual(actual_values_list, expected_values_list)

def get_expected_values(match_timeline_dto):
    # Extract expected values from the match_timeline_dto similar to the get_champion_stats function
    values_list = get_champion_stats(match_timeline_dto)
    expected_values = []

    for value in values_list:
        expected_dict = {
            'match_id': value['match_id'],
            'frame_number': value['frame_number'],
            'participant_id': value['participant_id'],
            'ability_haste': value['ability_haste'],
            'ability_power': value['ability_power'],
            'armor': value['armor'],
            'armor_pen': value['armor_pen'],
            'armor_pen_percent': value['armor_pen_percent'],
            'attack_damage': value['attack_damage'],
            'attack_speed': value['attack_speed'],
            'bonus_armor_pen_percent': value['bonus_armor_pen_percent'],
            'bonus_magic_pen_percent': value['bonus_magic_pen_percent'],
            'cc_reduction': value['cc_reduction'],
            'health': value['health'],
            'health_max': value['health_max'],
            'health_regen': value['health_regen'],
            'lifesteal': value['lifesteal'],
            'magic_pen': value['magic_pen'],
            'magic_pen_percent': value['magic_pen_percent'],
            'magic_resist': value['magic_resist'],
            'movement_speed': value['movement_speed'],
            'omnivamp': value['omnivamp'],
            'physical_vamp': value['physical_vamp'],
            'power': value['power'],
            'power_max': value['power_max'],
            'power_regen': value['power_regen'],
            'spell_vamp': value['spell_vamp']
        }
        expected_values.append(expected_dict)

    return expected_values


class TestGetBansFunction(TestCase):
    def test_get_bans(self):
        # Mock match_dto data
        mock_match_dto = {
            'info': {
                'gameId': '12345',
                'teams': [
                    {
                        'bans': [
                            {'championId': 1, 'pickTurn': 1},
                            {'championId': 2, 'pickTurn': 2}
                        ]
                    },
                    {
                        'bans': [
                            {'championId': 3, 'pickTurn': 1},
                            {'championId': 4, 'pickTurn': 2}
                        ]
                    }
                ]
            }
        }

        # Expected output
        expected_bans = [
            {'match_id': '12345', 'champion_id': 1, 'pick_turn': 1},
            {'match_id': '12345', 'champion_id': 2, 'pick_turn': 2},
            {'match_id': '12345', 'champion_id': 3, 'pick_turn': 1},
            {'match_id': '12345', 'champion_id': 4, 'pick_turn': 2},
        ]

        # Call the function with the mock data
        actual_bans = get_bans(mock_match_dto)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_bans, expected_bans)

