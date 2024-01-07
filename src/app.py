import streamlit as st
import psycopg2
from api_client import API_Client
import postgres_helperfile
from extract_data import insert_match
from match_classes import SummonerDto
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# postgres admin
ACCOUNT_IS_ADMIN = True

# NA1_4864820958
def main():
    st.title("League of Legends Summoner Lookup")

    summoner_name = st.text_input("Enter summoner name", placeholder="Enter summoner name")
    if summoner_name:
        try:
            logging.info(f"Fetching data for summoner: {summoner_name}")
            # API call to retrieve puuid from summoner names
            summoner_json = API_Client().get_summoner_by_name(summoner_name)
            summoner_dto = SummonerDto(summoner_json)
            summoner_puuid = summoner_dto.puuid
        except Exception as e:
            logging.error(f"Error fetching summoner data: {e}")
            st.error(f"Error fetching summoner data: {e}")
            return

        try:
            # API call to retrieve puuid's last 20 matches
            match_ids = API_Client().get_match_ids_by_puuid(summoner_puuid)
            logging.info(f"Retrieved match IDs for {summoner_name}")
            st.write(match_ids)
        except Exception as e:
            logging.error(f"Error fetching match IDs: {e}")
            st.error(f"Error fetching match IDs: {e}")
            return

        for match_id in match_ids:
            logging.info(f"Processing match ID: {match_id}")
            match_dto = API_Client().get_match_by_match_id(match_id)
            match_timeline_dto = API_Client().get_match_timeline(match_id)

            insert_match(match_dto, match_timeline_dto)

    st.subheader("SQL Query Execution")
    user_query = st.text_area("Enter your SQL query here:", height=100)
    if user_query:
        try:
            if ACCOUNT_IS_ADMIN:
                conn = postgres_helperfile.connect_db("admin")
            else:
                conn = postgres_helperfile.connect_db()

            with conn.cursor() as cursor:
                logging.info(f"Executing SQL query: {user_query}")
                cursor.execute(user_query)

                if user_query.strip().lower().startswith("select"):
                    rows = cursor.fetchall()
                    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
                    st.dataframe(df)  # Display in tabular format

        except psycopg2.Error as e:
            logging.error(f"Database error: {e}")
            if "permission denied" in str(e).lower():
                st.error("You don't have permission to execute this query.")
            else:
                st.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
