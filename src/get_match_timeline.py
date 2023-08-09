import requests
from get_API_key import get_API_key

def get_match_timeline(match_id):
    base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/{}/timeline?api_key={}'
    url = base_url.format(match_id, get_API_key())
    
    response = requests.get(url)
    
    if response.status_code == 200:
        match_timeline = response.json()
        return match_timeline
    else:
        print(f"Error: {response.status_code}")
        return None