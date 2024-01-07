import os
import logging
import json

from api_client import API_Client
from extract_data import *
from postgres_helperfile import SQLHelper, add_df_to_table, match_id_is_in_table

def main(match_id):
    logging.info("Starting main process for match ID: %s", match_id)
    api_client = API_Client()
    # get match_dto, match_timeline_dto
    match_dto = api_client.get_match_by_match_id(match_id)
    match_timeline_dto = api_client.get_match_timeline(match_id)

    if match_dto is None or match_timeline_dto is None:
        raise Exception('Riot API call failed. Check API key.')

    # Save to cache
    save_to_cache(f"match_{match_id}.json", match_dto)
    save_to_cache(f"timeline_{match_id}.json", match_timeline_dto)

    # try to insert
    try:
        insert_match(match_dto, match_timeline_dto)
    except Exception as e:
        logging.error(f"Failed to insert match data for match ID {match_id}: {e}")
        print(f"Failed to insert match data: {e}")
        raise

    # Upon successful insertion, clean up cache
    cleanup_cache(match_id)

def cleanup_cache(match_id):
    cache_dir = "./cache"
    match_file = os.path.join(cache_dir, f"match_{match_id}.json")
    timeline_file = os.path.join(cache_dir, f"timeline_{match_id}.json")

    try:
        if os.path.exists(match_file):
            os.remove(match_file)
            logging.info("Deleted cache file: %s", match_file)

        if os.path.exists(timeline_file):
            os.remove(timeline_file)
            logging.info("Deleted cache file: %s", timeline_file)
    except Exception as e:
        logging.error("Failed to clean up cache for match ID %s: %s", match_id, e)


def save_to_cache(filename, data):
    """Save data to a file in the cache directory."""
    cache_dir = "./cache"  # Change to a relative path
    os.makedirs(cache_dir, exist_ok=True)  # Create the cache directory if it doesn't exist
    file_path = os.path.join(cache_dir, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file)

def insert_participant_frames(table_name, participant_frames_list):
    helper = SQLHelper()
    for pframes in participant_frames_list:
        helper.insert_dict(table_name, pframes)


def insert_match(match_dto, match_timeline_dto):
    match_id = match_dto.metadata.match_id

    logging.info("Inserting match data for %s match DTO and timeline DTO", match_id)
    # Dictionary mapping table names to their respective data retrieval functions

    get_data_function_dict = {
        'match_metadata': lambda: get_match_metadata(match_dto),
        'perk_style_selections': lambda: get_perk_style_selections(match_dto),
        'participant_dto': lambda: get_participant_dto(match_dto),
        'challenges': lambda: get_challenges(match_dto),
        'victim_damage_dealt': get_victim_damage_dealt(match_timeline_dto),
        'vicim_damage_received': get_victim_damage_received(match_timeline_dto),
        'participant_frames': lambda: get_participant_frames(match_timeline_dto),
        'champion_stats': lambda: get_champion_stats(match_timeline_dto),
        'match_events': lambda: get_match_events(match_timeline_dto),
        'damage_stats': lambda: get_damage_stats(match_timeline_dto),
        'teams': lambda: get_teams(match_dto),
        'bans': lambda: get_bans(match_dto)
    }

    # Check which tables do not have that match data
    for table_name, get_data_function in get_data_function_dict.items():
        if match_id_is_in_table(table_name, match_id):
            if table_name == 'participant_frames':
                insert_participant_frames(table_name, get_data_function)
            else:
                add_df_to_table(table_name, get_data_function)
    
    logging.info("Data insertion for match %s completed successfully", match_id)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <match_id>")
        sys.exit(1)

    match_id = sys.argv[1]
    main(match_id)