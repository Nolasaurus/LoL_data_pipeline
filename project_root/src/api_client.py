import os
from dotenv import load_dotenv
import requests
import logging
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class RateLimitExceededError(Exception):
    pass

class APIKeyExpiredError(Exception):
    def __init__(self, message="API key has expired"):
        super().__init__(message)


class API_Client:
    def __init__(self):
        load_dotenv('./.env', verbose=True) 
        self.api_key = os.environ.get("RIOT_API_KEY")
        if not self.api_key:
            logging.error("API key is not set in environment variables")
            raise Exception("API key is not set in environment variables")
        logging.info(f"API key loaded: {self.api_key}")


    def _make_request(self, url, timeout=None):
        logging.debug(f"Making request to URL: {url} with API key: {self.api_key}")
        # Common code to make an HTTP request to the API
        try:
            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                print(response)
                raise APIKeyExpiredError("403: No Riot API key or key expired")
            elif response.status_code == 429:
                raise RateLimitExceededError("429: Rate limited. Too many API calls recently")
            else:
                print(f"Error: {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            print(f"Request timed out for url: {url}")
            return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Request exception: {e}")
            return None

    def get_summoner_by_name(self, summoner_name):
        # Remove leading/trailing whitespaces and encode space character
        summoner_name_encoded = summoner_name.strip().replace(" ", "%20")

        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response if response else None

    def get_match_ids_by_puuid(self, puuid, start=0, count=20):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={self.api_key}"
        return self._make_request(url, timeout=5)

    def get_match_by_match_id(self, match_id):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        if response:
            return response

    def get_match_timeline(self, match_id):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        if response:
            return response

    def get_puuid_by_summon_id(self, summoner_id):
        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response["puuid"] if response else None

    def get_summoner_ids_from_league_id(self, league_id):
        url = f"https://na1.api.riotgames.com/lol/league/v4/leagues/{league_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        if response:
            summoner_ids = [entry["summonerId"] for entry in response["entries"]]
            return summoner_ids
        else:
            return None


if __name__ == "__main__":
    client = API_Client()