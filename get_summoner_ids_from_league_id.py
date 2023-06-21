import requests

def get_summoner_ids_from_league_id(league_id, API_key):
    base_url = 'https://na1.api.riotgames.com/lol/league/v4/leagues/{league_id}?api_key={API_key}'
    url = base_url.format(API_key=API_key, league_id=league_id)
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        summoner_ids = [entry['summonerId'] for entry in data['entries']]
        return summoner_ids
    else:
        print(f"Error: {response.status_code}")
        return None