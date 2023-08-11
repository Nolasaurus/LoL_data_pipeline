import requests
from src.get_API_key import get_API_key

# get PUU-id from summoner name
def get_puuid_by_name(summoner_name):
    summoner_name = summoner_name.strip()  # Remove leading and trailing whitespaces
    summoner_name_encoded = summoner_name.replace(" ", "%20") # encode space character
    base_url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_key}'
    url = base_url.format(API_key=get_API_key(), summoner_name=summoner_name_encoded)
   
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
       return data['puuid']
    else:
        print(f"Error: {response.status_code}")
        return None