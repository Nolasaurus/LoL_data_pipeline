import os
from dotenv import load_dotenv
import requests
import logging
import time

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class RateLimitExceededError(Exception):
    pass


class APIKeyExpiredError(Exception):
    def __init__(self, message="API key has expired"):
        super().__init__(message)


class RateLimiter:
    def __init__(self, max_requests, period):
        self.max_requests = max_requests
        self.period = period
        self.timestamps = []

    def __call__(self):
        now = time.time()
        self.timestamps = [ts for ts in self.timestamps if ts > now - self.period]

        if len(self.timestamps) < self.max_requests:
            self.timestamps.append(now)
        else:
            oldest_request = min(self.timestamps)
            time_to_wait = self.period - (now - oldest_request)
            time.sleep(time_to_wait)
            self.timestamps.append(time.time())


rl_sec = RateLimiter(20, 1)  # 20 requests per 1 second
rl_min = RateLimiter(100, 120)  # 100 requests per 2 minutes


class API_Client:
    def __init__(self):
        load_dotenv(".env", verbose=True)  # Construct the correct path
        self.api_key = os.environ.get("RIOT_API_KEY")
        if not self.api_key:
            logging.error("API key is not set in environment variables")
            raise Exception("API key is not set in environment variables")
        logging.info("API key loaded")

    def _make_request(self, url, timeout=None):
        logging.debug("Making request to URL: %s", url)

        # Enforce rate limiting before making a request
        rl_sec()
        rl_min()

        # Common code to make an HTTP request to the API
        try:
            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                raise APIKeyExpiredError(f"403: Riot API key expired, {response}")
            elif response.status_code == 429:
                raise RateLimitExceededError(
                    "429: Rate limited. Too many API calls recently"
                )
            else:
                print(f"Error: {response.status_code}")
                return None

        except requests.exceptions.Timeout:
            logging.error(f"Request timed out for url: {url}")
            return None
        except requests.exceptions.RequestException as e:
            logging.error("Request exception: %s", e)
            return None
        except Exception as e:
            logging.error("An unexpected error occurred during request: %s", e)
            return None

    def get_summoner_by_name(self, summoner_name):
        logging.info(f"Fetching summoner data for: {summoner_name}")
        # Remove leading/trailing whitespaces and encode space character
        summoner_name_encoded = summoner_name.strip().replace(" ", "%20")
        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response if response else None

    def get_match_ids_by_puuid(self, puuid, start=0, count=20):
        logging.info(f"Fetching match IDs for PUUID: {puuid}")
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response if response else None

    def get_match_by_match_id(self, match_id):
        logging.info(f"Fetching match data for match ID: {match_id}")
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response if response else None

    def get_match_timeline(self, match_id):
        logging.info(f"Fetching match timeline for match ID: {match_id}")
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response if response else None

    def get_puuid_by_summon_id(self, summoner_id):
        logging.info(f"Fetching PUUID for summoner ID: {summoner_id}")
        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response["puuid"] if response else None

    def get_summoner_ids_from_league_id(self, league_id):
        logging.info(f"Fetching summoner IDs for league ID: {league_id}")
        url = f"https://na1.api.riotgames.com/lol/league/v4/leagues/{league_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        if response:
            summoner_ids = [entry["summonerId"] for entry in response["entries"]]
            return summoner_ids
        else:
            return None
