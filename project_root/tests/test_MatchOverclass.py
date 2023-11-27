import pytest
from unittest.mock import MagicMock
from project_root.src.MatchOverclass import MatchOverclass
from project_root.src.MatchDto import MetadataDto, InfoDto
from project_root.src.MatchTimelineDto import Metadata, Info
import json

def load_mocked_timeline_response():
    with open('tests/files/NA1_4729149632_match_timeline.json', 'r') as file:
        return json.load(file)

def load_mocked_match_data_response():
    with open('tests/files/NA1_4729149632_match_data.json', 'r') as file:
        return json.load(file)

def test_match_timeline_dto_initialization():
    mocked_api_client = MagicMock()
    mocked_response = load_mocked_timeline_response()
    mocked_api_client.get_match_timeline.return_value = mocked_response

    match_id = "NA1_4729149632"
    match_timeline = MatchOverclass.get_match_timeline_dto(match_id, mocked_api_client)
 
    assert match_timeline.metadata.matchId == "NA1_4729149632"
    assert isinstance(match_timeline.metadata, Metadata)
    assert isinstance(match_timeline.info, Info)

def test_match_dto_initialization():
    mocked_api_client = MagicMock()
    mocked_response = load_mocked_match_data_response()
    mocked_api_client.get_match_by_match_id.return_value = mocked_response

    match_id = "NA1_4729149632"
    match_dto = MatchOverclass.get_match_dto(match_id, mocked_api_client)

    assert match_dto.match_id == "NA1_4729149632"
    assert isinstance(match_dto.metadata, MetadataDto)
    assert isinstance(match_dto.info, InfoDto)
