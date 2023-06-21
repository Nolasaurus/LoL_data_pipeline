import requests

def getMatchTimeline(match_id, API_key):
    base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/{}/timeline?api_key={}'
    url = base_url.format(match_id, API_key)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        match_timeline = response.json()
        return match_timeline
    else:
        print(f"Error: {response.status_code}")
        return None