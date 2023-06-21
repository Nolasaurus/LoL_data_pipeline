import requests
def get_match_ids_by_puuid(puu_id, API_key, start=0, count=3):
    base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={API_key}'
    url = base_url.format(puu_id=puu_id, start=start, count=count, API_key=API_key)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json() 
    else:
        print(f"Error: {response.status_code}")
        return None

