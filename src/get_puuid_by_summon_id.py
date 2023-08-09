import requests
from src.get_API_key import get_API_key

# get PUU-id from summonerId
def get_puuid_by_summon_id(summoner_id):
    base_url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={API_key}'
    url = base_url.format(API_key=get_API_key(), summoner_id=summoner_id)
   
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
       return data['puuid']
    else:
        print(f"Error: {response.status_code}")
        return None