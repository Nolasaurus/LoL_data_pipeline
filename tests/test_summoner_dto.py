import pytest
from unittest.mock import MagicMock
from api_client import API_Client
from SummonerDto import SummonerDto  # Replace 'your_module' with the actual module name

def test_get_summoner_dto():
    # Mock the API_Client and its get_summoner_by_name method
    API_Client.get_summoner_by_name = MagicMock(return_value={
        "accountId": "test_account_id",
        "profileIconId": 1234,
        "revisionDate": 1618500000000,
        "name": "TestName",
        "id": "test_id",
        "puuid": "test_puuid",
        "summonerLevel": 30
    })

    # Call the method
    summoner_dto = SummonerDto.get_summoner_dto("TestName")

    # Asserts
    assert summoner_dto.name == "TestName"
    assert summoner_dto.puuid == "test_puuid"
    assert summoner_dto.summoner_level == 30

    # Clean up
    API_Client.get_summoner_by_name = MagicMock()  # Reset the mock
