from src.connect_db import connect_db
conn = connect_db()

def parse_match_json(match_json):
    match = match_json
    # MetadataDto fields
    data_version = match['metadata']['dataVersion']
    match_id = match['metadata']['matchId']
    participants_puuids = match['metadata']['participants']

    # InfoDto fields
    game_start = match['info']['gameCreation']
    game_length = match['info']['gameDuration']
    game_id = match['info']['gameId']
    game_mode = match['info']['gameMode']
    game_name = match['info']['gameName']
    game_start_timestamp = match['info']['gameStartTimestamp']
    game_end_timestamp = match['info'].get('gameEndTimestamp', None)
    game_type = match['info']['gameType']
    game_version = match['info']['gameVersion']
    map_id = match['info']['mapId']
    platform_id = match['info']['platformId']
    queue_id = match['info']['queueId']
    tournament_code = match['info'].get('tournamentCode', None)

    # Insert into match_data
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO match_data (match_id, data_version, game_start, game_length, game_end_timestamp, game_id, game_mode, game_name, game_start_timestamp, game_type, game_version, map_id, platform_id, queue_id, tournament_code)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (match_id, data_version, game_start, game_length, game_end_timestamp, game_id, game_mode, game_name, game_start_timestamp, game_type, game_version, map_id, platform_id, queue_id, tournament_code))