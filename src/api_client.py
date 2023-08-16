import requests
from src.get_API_key import get_API_key

class API_client:
    def __init__(self):
        self.api_key = get_API_key()

    def _make_request(self, url, timeout=None):
        # Common code to make an HTTP request to the API
        try:
            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            print(f"Request timed out for url: {url}")
            return None
        
    def get_puuid_by_name(self, summoner_name):
        summoner_name_encoded = summoner_name.strip().replace(" ", "%20") # remove leading/trailing whitespaces and encode space character
        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}'

        response = self._make_request(url, timeout=5)
        if response is not None:
            # update player table
            return response['puuid']
        else:
            # Handle the case where the request fails
            return None

    
    def get_match_ids_by_puuid(self, puu_id, start=0, count=20):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={self.api_key}'
        # update player_match table first
        return self._make_request(url, timeout=5)

    def get_match_by_match_id(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}'
        # update match_data table first
        return self._make_request(url, timeout=5)

    def get_match_timeline(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}'
        # update match_timeline table first
        return self._make_request(url, timeout=5)
