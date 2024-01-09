import os
import logging
import json
from api_client import API_Client
from extract_data import *
from postgres_helperfile import create_engine


def cached_insert(match_id):
    logging.info("Starting main process for match ID: %s", match_id)
    api_client = API_Client()
    # get match_dto, match_timeline_dto
    match_dto = api_client.get_match_by_match_id(match_id)
    match_timeline_dto = api_client.get_match_timeline(match_id)

    if match_dto is None or match_timeline_dto is None:
        raise Exception("Riot API call failed. Check API key.")

    # Save to cache
    save_to_cache(f"match_{match_id}.json", match_dto)
    save_to_cache(f"timeline_{match_id}.json", match_timeline_dto)

    # try to insert
    try:
        insert_match(match_dto, match_timeline_dto)
    except Exception as e:
        logging.error("Failed to insert match data for match ID %s: %s", match_id, e)
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
    os.makedirs(
        cache_dir, exist_ok=True
    )  # Create the cache directory if it doesn't exist
    file_path = os.path.join(cache_dir, filename)
    with open(file_path, "w") as file:
        json.dump(data, file)


def insert_match(match_dto, match_timeline_dto):
    data_match_id = match_dto.get("metadata").get("matchId")
    # Ensure you have the correct parameters to create_engine here
    engine = create_engine()  # Provide the correct database URL here
    logging.info(
        "Inserting match data for %s match DTO and timeline DTO", data_match_id
    )

    get_bans(match_dto).to_sql("bans", engine, if_exists="append", index=False)
    get_challenges(match_dto).to_sql(
        "challenges", engine, if_exists="append", index=False
    )
    get_champion_stats(match_timeline_dto).to_sql(
        "champion_stats", engine, if_exists="append", index=False
    )
    get_damage_stats(match_timeline_dto).to_sql(
        "damage_stats", engine, if_exists="append", index=False
    )
    get_match_events(match_timeline_dto).to_sql(
        "match_events", engine, if_exists="append", index=False
    )
    get_match_metadata(match_dto).to_sql(
        "match_metadata", engine, if_exists="append", index=False
    )
    get_participant_dto(match_dto).to_sql(
        "participant_dto", engine, if_exists="append", index=False
    )
    get_participant_frames(match_timeline_dto).to_sql(
        "participant_frames", engine, if_exists="append", index=False
    )
    get_perk_style_selections(match_dto).to_sql(
        "perk_style_selections", engine, if_exists="append", index=False
    )
    get_teams(match_dto).to_sql("teams", engine, if_exists="append", index=False)
    get_victim_damage_dealt(match_timeline_dto).to_sql(
        "victim_damage_dealt", engine, if_exists="append", index=False
    )
    get_victim_damage_received(match_timeline_dto).to_sql(
        "victim_damage_received", engine, if_exists="append", index=False
    )

    logging.info("Data insertion for match %s completed successfully", data_match_id)
