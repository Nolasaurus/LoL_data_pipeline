from src.connect_db import connect_db
from src.api_client import API_client

class RecordHandler:
    def __init__(self):
        # Ensure the database is available
        self.conn = self._connect_to_db()
        self.api_client = API_client()  # Create an instance of the API_client class


    def _connect_to_db(self):
        try:
            return connect_db()
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def check_db_for_summoner_name(self, summoner_name):
        if not self.conn:
            print("Database connection is not available.")
            return None

        cursor = self.conn.cursor()
        try:
            # Query the 'summoner' table for the summoner_name
            cursor.execute("SELECT * FROM summoner WHERE name=%s", (summoner_name,))
            row = cursor.fetchone()

            if row:
                return row[1]
            else:
                # If the summoner_name doesn't exist in the database, fetch it from the API
                puuid = self.api_client.get_puuid_by_name(summoner_name)
                cursor.execute("INSERT INTO summoner (name, puuid) VALUES (%s, %s)", (summoner_name, puuid))
                self.conn.commit()
                return puuid

        except Exception as e:
            print(f"Error querying the database: {e}")
            return None

    def check_db_for_match_ids(self, puuid):
        if not self.conn:
            print("Database connection is not available.")
            return None

        cursor = self.conn.cursor()
        try:
            # Query the 'match_ids' table for the puuid
            cursor.execute("SELECT match_id FROM match_ids WHERE puuid=%s", (puuid,))
            rows = cursor.fetchall()

            if rows:
                # Extract match_ids from the rows and return them
                return [row[0] for row in rows]
            else:
                # If the puuid doesn't exist in the database, fetch it from the API
                match_ids = self.api_client.get_match_ids_by_puuid(puuid)
                # TODO: add START and STOP and COUNT to api call
                for id in match_ids:
                    cursor.execute("INSERT INTO match_ids (puuid, match_id) VALUES (%s, %s)", (puuid, id))
                
                # Commit the transaction after all inserts
                self.conn.commit()
                
                return match_ids

        except Exception as e:
            print(f"Error querying the database: {e}")
            return None

    def check_db_for_match(self, match_id):
        if not self.conn:
            print("Database connection is not available.")
            return None

        cursor = self.conn.cursor()
        try:
            # Query the 'match' table for the match_id
            cursor.execute("SELECT match_json, match_timeline_json FROM match WHERE match_id=%s", (match_id,))
            row = cursor.fetchone()

            if row:
                return row[0], row[1]
            else:
                # If the match_id doesn't exist in the database, fetch it from the API
                match_json = self.api_client.get_match_by_match_id(match_id)
                match_timeline_json = self.api_client.get_match_timeline(match_id)
                cursor.execute("INSERT INTO match (match_id, match_json, match_timeline_json) VALUES (%s, %s, %s)", 
                               (match_id, match_json, match_timeline_json))
                self.conn.commit()
                return match_json, match_timeline_json

        except Exception as e:
            print(f"Error querying the database: {e}")
            return None
