import os
import requests
import webbrowser
import subprocess
import sys


class APIKeyExpiredError(Exception):
    def __init__(self, message="API key has expired"):
        super().__init__(message)
        self.open_browser()

    def open_browser(self):
        url = "https://developer.riotgames.com/login"
        if sys.platform == "win32":
            # If the script is running on native Windows Python, use webbrowser.
            webbrowser.open(url)
        else:
            # If the script is running in WSL, use `cmd.exe /C start`.
            try:
                subprocess.run(['cmd.exe', '/C', 'start', url], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to open browser: {e}")

class API_Client:
    def __init__(self):
        self.api_key = os.environ.get("RIOT_API_KEY")

    def _make_request(self, url, timeout=None):
        # Common code to make an HTTP request to the API
        try:
            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                raise APIKeyExpiredError("Riot API key expired")
            else:
                print(f"Error: {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            print(f"Request timed out for url: {url}")
            return None

    def get_puuid_by_name(self, summoner_name):
        summoner_name_encoded = summoner_name.strip().replace(
            " ", "%20"
        )  # Remove leading/trailing whitespaces and encode space character
        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        return response["puuid"] if response else None

    def get_match_ids_by_puuid(self, puu_id, start=0, count=20):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={self.api_key}"
        return self._make_request(url, timeout=5)

    def get_match_by_match_id(self, match_id):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        if response:
            # make POST request to this endpoint
            endpoint = "http://localhost:6789/api/pipeline_schedules/2/pipeline_runs/4df48ebbba94456eb4209e0d1bbef064"
            post_response = requests.post(endpoint, json=response, timeout=5)

    def get_match_timeline(self, match_id):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}"
        response = self._make_request(url, timeout=5)
        if response:
            # make POST request to this endpoint
            endpoint = "http://localhost:6789/api/pipeline_schedules/1/pipeline_runs/15d312a470f545ea8592e8848b4d08dc"
            post_response = requests.post(endpoint, json=response, timeout=5)

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
