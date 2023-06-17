# league IDs
# https://canisback.com/leagueId/

import pandas as pd
import requests



import pandas as pd
import requests

url = 'https://canisback.com/leagueId/league_na1.csv'
response = requests.get(url, verify=False)

# Save the response content to a file
with open('league_na1.csv', 'w') as file:
    file.write(response.text)

# Read the CSV file using pandas
na1_csv = pd.read_csv('league_na1.csv')
league_dict = {}

tiers = na1_csv.tier.unique()

for tier in tiers: 
    leagues_in_tier = na1_csv[na1_csv['tier'] == tier]
    league_dict[tier] = leagues_in_tier

'''
Rate Limits:
20 requests every 1 seconds(s)
100 requests every 2 minutes(s)
'''


# TODO: def checkRateLimit():

def getMatchIdsByPUUidhTimeline(puu_id,  API_key, start=0, count=20):
    base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={API_key}'
    url = base_url.format(puu_id=puu_id, start=start, count=count, API_key=API_key)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        match_ids = response.json()
        return match_ids 
    else:
        print(f"Error: {response.status_code}")
        return None

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







# get league
# https://developer.riotgames.com/apis#league-v4/GET_getGrandmasterLeague

# get puuid by summonerid
# https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerId

# get match ids by puuid
# https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID

# get match timeline
# https://developer.riotgames.com/apis#match-v5/GET_getTimeline

# or get match
# https://developer.riotgames.com/apis#match-v5/GET_getMatch

