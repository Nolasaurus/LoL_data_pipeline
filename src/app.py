import streamlit as st
import psycopg2
from api_client import API_Client
import postgres_helperfile
from insert_match import insert_match
from match_classes import SummonerDto

DEV_MODE = False # postgres


def main():
    st.title("League of Legends Summoner Lookup")

    summoner_name = st.text_input(
        "Enter summoner name", placeholder="Enter summoner name"
    )
    if summoner_name:
        try:
            # API call to retrieve puuid from summoner names
            summoner_json = API_Client().get_summoner_by_name(summoner_name)
            summoner_dto = SummonerDto(summoner_json)
            summoner_puuid = summoner_dto.puuid
        except Exception as e:
            st.error(f"Error fetching summoner data: {e}")
            return

        try:
            # API call to retrieve puuid's last 20 matches
            match_ids = API_Client().get_match_ids_by_puuid(summoner_puuid)
            st.write(match_ids)
        except Exception as e:
            st.error(f"Error fetching match IDs: {e}")
            return

        for match_id in match_ids:
            print(match_id)
            match_dto = API_Client().get_match_by_match_id(match_id)
            match_timeline_dto = API_Client().get_match_timeline(match_id)

            insert_match(match_dto, match_timeline_dto)

    st.subheader("SQL Query Execution")
    user_query = st.text_area("Enter your SQL query here:", height=100)
    if user_query:  # Execute the query whenever text area input
        try:
            if DEV_MODE:
                conn = postgres_helperfile.connect_db("admin")
            else:
                conn = postgres_helperfile.connect_db()

            with conn.cursor() as cursor:
                cursor.execute(user_query)

                if user_query.strip().lower().startswith("select"):
                    rows = cursor.fetchall()
                    st.write(rows)
                else:
                    conn.commit()
                    st.success("Query executed successfully")

        except psycopg2.Error as e:
            if "permission denied" in str(e).lower():
                st.error("You don't have permission to execute this query.")
            else:
                st.error(f"Database error: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
