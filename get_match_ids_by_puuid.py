import requests

from get_API_key import get_API_key
def get_match_ids_by_puuid(puu_id, start=0, count=20):
    base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={API_key}'
    url = base_url.format(puu_id=puu_id, start=start, count=count, API_key=get_API_key())
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json() 
    else:
        print(f"Error: {response.status_code}")
        return None

