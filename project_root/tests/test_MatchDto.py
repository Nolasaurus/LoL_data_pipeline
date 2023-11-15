import os
import pytest
from unittest.mock import patch, MagicMock
import json
from backend.src.MatchDto import MatchDto, MetadataDto, InfoDto
from backend.src.api_client import API_Client


def load_mocked_response():
    with open(os.path.join('tests', 'files', 'NA1_4729149632_match_data.json'), 'r') as file:
        return json.load(file)

mocked_response = load_mocked_response()

@pytest.fixture
def api_client_mock():
    with patch('backend.src.MatchDto.API_Client') as mock:
        instance = mock.return_value
        instance.get_match_by_match_id.return_value.json.return_value = mocked_response
        yield instance


def test_match_dto_initialization(api_client_mock):
    match_id = "NA1_4729149632"
    match_dto = MatchDto.get_match_dto(match_id)

    assert match_dto.match_id == "NA1_4729149632"
    assert isinstance(match_dto.metadata, MetadataDto)
    assert isinstance(match_dto.info, InfoDto)