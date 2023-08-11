import requests
from src.get_API_key import get_API_key
from src.upload_matches import insert_or_update

def get_match_by_match_id(match_id):
    """
    Retrieves match data and match timeline for a given match ID from the Riot Games API.

    Parameters:
        match_id (str): The ID of the match to retrieve.

    Returns:
        tuple: A tuple containing the match data and match timeline as JSON objects if successful.
               Returns None if an error occurs or if the request times out.

    Example:
        match_data, match_timeline = get_match_by_match_id("NA1_3720451304")
    """

    base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/{}?api_key={}'
    url = base_url.format(match_id, get_API_key())
    tl_base_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/{}/timeline?api_key={}'
    tl_url = tl_base_url.format(match_id, get_API_key())
    
    try:
        response = requests.get(url, timeout=5)
        tl_response = requests.get(tl_url, timeout=5)

        if tl_response.status_code == 200:
            match_timeline = tl_response.json()

        if response.status_code == 200:
            match_data = response.json()
            insert_or_update(match_id, match_data, match_timeline)
            return match_data, match_timeline
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.Timeout:
        print(f"Request timed out for match_id: {match_id}")
        return None
