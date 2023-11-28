import streamlit as st
import psycopg2
from SummonerDto import SummonerDto
from api_client import API_Client
import postgres_helperfile  # Ensure postgres_helperfile is in your project directory

def main():
    st.title("League of Legends Summoner Lookup")

    summoner_name = st.text_input("Enter summoner name", placeholder="Enter summoner name")
    if summoner_name:
        try:
            # API call to retrieve puuid from summoner name
            summoner_dto = SummonerDto.get_summoner_dto(summoner_name)
            summoner_puuid = summoner_dto.puuid
        except Exception as e:
            st.error(f"Error fetching summoner data: {e}")
            return 

        try:
            # API call to retrieve puuid's last 20 matches
            match_ids = API_Client().get_match_ids_by_puuid(summoner_puuid)
            most_recent_match_id = match_ids[0]
            st.write(match_ids)
        except Exception as e:
            st.error(f"Error fetching match IDs: {e}")
            return

    st.subheader("SQL Query Execution")
    user_query = st.text_area("Enter your SQL query here:", height=100)
    if user_query:  # Execute the query whenever text area input
        try:
            with postgres_helperfile.connect_db() as conn:
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