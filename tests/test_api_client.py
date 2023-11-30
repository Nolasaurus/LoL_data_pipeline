import json
from unittest.mock import patch
from api_client import API_Client

# Test class for GetMatchByMatchId
@patch('api_client.requests.get')
def test_get_match_by_match_id_successful(mock_get):
    with open('tests/files/NA1_4729149632_match_data.json', 'r') as file:
        expected_match_data = json.load(file)

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = expected_match_data

    match_id = 'NA1_4729149632'
    client = API_Client()
    result = client.get_match_by_match_id(match_id)

    assert result == expected_match_data


@patch('api_client.requests.get')
def test_get_match_by_match_id_failure(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    match_id = 'invalid_match_id'
    client = API_Client()
    result = client.get_match_by_match_id(match_id)

    assert result is None


# Test class for GetMatchIdsByPuuid
@patch('api_client.requests.get')
def test_get_match_ids_by_puuid_successful(mock_get):
    expected_match_ids = ["NA1_4656725054", "NA1_4656701593", "NA1_4644336325"]

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = expected_match_ids

    puu_id = 'QeQevDlzR9buXaCEj3GqHyV9ZWxMrs-ltqdgsReyS7_Lu1wuMKhv7xqybkCEbRNHmn2OlqoS_xYjhw'
    client = API_Client() 
    result = client.get_match_ids_by_puuid(puu_id, start=0, count=3)

    assert result == expected_match_ids


@patch('api_client.requests.get')
def test_get_match_ids_by_puuid_failure(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    puu_id = 'invalid_puu_id'
    client = API_Client()
    result = client.get_match_ids_by_puuid(puu_id)

    assert result is None


# Test class for GetMatchTimeline
@patch('api_client.requests.get')
def test_get_match_timeline_successful(mock_get):
    with open('tests/files/NA1_4729149632_match_timeline.json', 'r') as file:
        expected_timeline_data = json.load(file)

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = expected_timeline_data

    match_id = 'NA1_4729149632'
    result = API_Client().get_match_timeline(match_id)

    assert result == expected_timeline_data


@patch('api_client.requests.get')
def test_get_match_timeline_failure(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    match_id = 'invalid_match_id'
    result = API_Client().get_match_timeline(match_id)

    assert result is None


# Test class for GetPuuidByName
@patch('api_client.requests.get')
def test_get_puuid_by_name_successful(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {'puuid': 'aWzZ7KxMV8LGxgdrCOYQ4Mc8WXoVcH0l6QxLxUkiFNfP98derWmOax6lMGyU7mONopTrx13jm0qU0A'}

    summoner_name = 'The Steina'
    result = API_Client().get_summoner_by_name(summoner_name)

    assert result['puuid'] == 'aWzZ7KxMV8LGxgdrCOYQ4Mc8WXoVcH0l6QxLxUkiFNfP98derWmOax6lMGyU7mONopTrx13jm0qU0A'


@patch('api_client.requests.get')
def test_get_puuid_by_name_failure(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    summoner_name = 'InvalidSummonerName'
    result = API_Client().get_summoner_by_name(summoner_name)

    assert result is None