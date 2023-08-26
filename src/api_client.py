import requests
import json
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
        
    def get_SummonerDTO_by_name(self, summoner_name):
        # remove leading/trailing whitespaces and encode space character
        summoner_name_encoded = summoner_name.strip().replace(" ", "%20")

        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}'
<<<<<<< HEAD
        response = self._make_request(url, timeout=5)
        if response is not None:
            # update player table
            return response['puuid']
        else:
            # Handle the case where the request fails
            return None



    def get_match_by_match_id(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}'
        response = self._make_request(url, timeout=5)
        if response and isinstance(response, str):
            return json.loads(response)
        return response
=======
        return self._make_request(url, timeout=5 ) # JSON
>>>>>>> c8b4acf (rename to match official API)
    
    def get_matches_by_puuid(self, puu_id, start=0, count=20):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={self.api_key}'
<<<<<<< HEAD
=======
        # return value: List[string]
>>>>>>> c8b4acf (rename to match official API)
        return self._make_request(url, timeout=5)

    def get_MatchDto_by_match_id(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}'
<<<<<<< HEAD
        response = self._make_request(url, timeout=5)
        if response and isinstance(response, str):
            return json.loads(response)
        return response
=======
        return self._make_request(url, timeout=5) # JSON
>>>>>>> c8b4acf (rename to match official API)

    def get_MatchTimelineDto_by_match_id(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}'
<<<<<<< HEAD
        response = self._make_request(url, timeout=5)
        if response and isinstance(response, str):
            return json.loads(response)
        return response

    def get_puuid_by_name(self, summoner_name):
        summoner_name_encoded = summoner_name.strip().replace(" ", "%20") # Remove leading/trailing whitespaces and encode space character
        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}'
        response = self._make_request(url)
        return response['puuid'] if response else None

    def get_puuid_by_summon_id(self, summoner_id):
        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={self.api_key}'
        response = self._make_request(url)
        return response['puuid'] if response else None
    
    def get_summoner_ids_from_league_id(self, league_id):
        url = f'https://na1.api.riotgames.com/lol/league/v4/leagues/{league_id}?api_key={self.api_key}'
        response = self._make_request(url)
        if response:
            summoner_ids = [entry['summonerId'] for entry in response['entries']]
            return summoner_ids
        else:
            return None

=======
        return self._make_request(url, timeout=5) # JSON
>>>>>>> c8b4acf (rename to match official API)