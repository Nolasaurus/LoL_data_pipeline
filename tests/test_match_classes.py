import json
import pytest
from unittest.mock import MagicMock
from match_classes import MatchTimelineDto, MatchDto, SummonerDto

# Load mocked responses from JSON files
def load_mocked_response(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Test for MatchTimelineDto initialization
def test_match_timeline_dto_initialization():
    # Load mocked timeline response
    mocked_timeline_response = load_mocked_response('tests/files/NA1_4729149632_match_timeline.json')

    # Test initialization
    match_timeline_dto = MatchTimelineDto(mocked_timeline_response)

    # Assertions
    assert match_timeline_dto.metadata.match_id == "NA1_4729149632"
    assert isinstance(match_timeline_dto.metadata, MatchTimelineDto.Metadata)
    assert isinstance(match_timeline_dto.info, MatchTimelineDto.Info)


def test_match_dto_initialization():
    # Load mocked match data response
    mocked_match_data_response = load_mocked_response('tests/files/NA1_4729149632_match_data.json')

    # Test initialization
    match_dto = MatchDto(mocked_match_data_response)  # Pass the actual JSON response

    # Assertions
    assert match_dto.metadata.match_id == "NA1_4729149632"
    assert isinstance(match_dto.metadata, MatchDto.MetadataDto)
    assert isinstance(match_dto.info, MatchDto.InfoDto)

# def test_summoner_dto_init():

