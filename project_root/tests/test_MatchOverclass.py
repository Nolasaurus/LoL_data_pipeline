import json
import pytest
from unittest.mock import MagicMock
from MatchOverclass import MatchOverclass
from MatchDto import MetadataDto, InfoDto
from MatchTimelineDto import Metadata, Info

# Load mocked responses from JSON files
def load_mocked_response(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Test for MatchTimelineDto initialization
def test_match_timeline_dto_initialization():
    # Set up mocked API client and response
    mocked_api_client = MagicMock()
    mocked_timeline_response = load_mocked_response('tests/files/NA1_4729149632_match_timeline.json')
    mocked_api_client.get_match_timeline.return_value = mocked_timeline_response

    # Test initialization
    match_id = "NA1_4729149632"
    match_timeline_dto = MatchOverclass.get_match_timeline_dto(match_id, mocked_api_client)

    # Assertions
    assert match_timeline_dto.metadata.matchId == match_id
    assert isinstance(match_timeline_dto.metadata, Metadata)
    assert isinstance(match_timeline_dto.info, Info)

# Test for MatchDto initialization
def test_match_dto_initialization():
    # Set up mocked API client and response
    mocked_api_client = MagicMock()
    mocked_match_data_response = load_mocked_response('tests/files/NA1_4729149632_match_data.json')
    mocked_api_client.get_match_by_match_id.return_value = mocked_match_data_response

    # Test initialization
    match_id = "NA1_4729149632"
    match_dto = MatchOverclass.get_match_dto(match_id, mocked_api_client)
    print(match_dto.metadata, MetadataDto)
    print(match_dto.info, InfoDto)
    # Assertions
    assert match_dto.match_id == match_id
    assert isinstance(match_dto.metadata, MetadataDto)
    assert isinstance(match_dto.info, InfoDto)
