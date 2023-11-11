import json
from psycopg2 import sql
import sys
from connect_db import connect_db
from api_client import API_Client

def create_table():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS match (
                    match_id TEXT PRIMARY KEY,
                    match JSON NOT NULL,
                    match_timeline JSON
                );
            """)
            conn.commit()

def insert_or_update(match_id, match_data, match_timeline_data=None):
    with connect_db() as conn:
        with conn.cursor() as cur:
            insert_query = sql.SQL("""
                INSERT INTO match (match_id, match, match_timeline)
                VALUES (%s, %s, %s)
                ON CONFLICT (match_id)
                DO UPDATE SET match = %s, match_timeline = %s;
            """)
            cur.execute(insert_query, (match_id, json.dumps(match_data), json.dumps(match_timeline_data), json.dumps(match_data), json.dumps(match_timeline_data)))
            conn.commit()

def get_and_insert_match(match_id):
    api_client = API_Client()
    try:
        # Call the get_match_by_match_id.py script with the match_id as an argument
        match_data = api_client.get_match_by_match_id(match_id)
        match_data = json.dumps(match_data)

        # Call the get_match_timeline.py script with the match_id as an argument
        match_timeline_data = api_client.get_match_timeline(match_id)
        match_timeline_data = json.dumps(match_timeline_data)

        # Insert or update the data in the 'match' table
        insert_or_update(match_id, match_data, match_timeline_data)
        print(f"Successfully inserted/updated match_id: {match_id}")

    except Exception as e:
        print(f"An error occurred while processing match_id {match_id}: {e}")
        

def main():
    create_table()
    if len(sys.argv) > 1:
        match_id = sys.argv[1]
        get_and_insert_match(match_id)

if __name__ == "__main__":
    main()
