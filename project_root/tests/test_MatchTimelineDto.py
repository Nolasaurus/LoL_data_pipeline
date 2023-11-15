import os
import pytest
from unittest.mock import patch, MagicMock
import json
from backend.src.MatchTimelineDto import MatchTimelineDto, Metadata, Info
from backend.src.api_client import API_Client


def load_mocked_response():
    with open(os.path.join('tests', 'files', 'NA1_4729149632_match_timeline.json'), 'r') as file:
        return json.load(file)

mocked_response = load_mocked_response()

@pytest.fixture
def api_client_mock():
    with patch('backend.src.MatchTimelineDto.API_Client') as mock:
        instance = mock.return_value
        instance.get_match_timeline.return_value.json.return_value = mocked_response
        yield instance


def test_match_timeline_dto_initialization(api_client_mock):
    match_id = "NA1_4729149632"
    match_timeline = MatchTimelineDto.get_match_timeline_dto(match_id)

    assert match_timeline.metadata.matchId == "NA1_4729149632"
    assert isinstance(match_timeline.metadata, Metadata)
    assert isinstance(match_timeline.info, Info)