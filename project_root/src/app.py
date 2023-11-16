import traceback
import streamlit as st
from MatchOverclass import MatchOverclass
from SummonerDto import SummonerDto
from api_client import API_Client

client = API_Client()


def main():
    st.title("League of Legends Summoner Lookup")
    summoner_name = st.text_input(
        "Enter summoner name", placeholder="Enter summoner name"
    )

    if summoner_name:
        try:  # API call to retrieve puuid from summoner name
            summoner_dto = SummonerDto.get_summoner_dto(summoner_name)
            summoner_puuid = summoner_dto.puuid
        except Exception as e:
            st.error(f"Error fetching summoner data: {e}")
            return

        try:  # API call to retrieve puuid's last 20 matches
            match_ids = client.get_match_ids_by_puuid(summoner_puuid)
            most_recent_match_id = match_ids[0]
        except Exception as e:
            st.error(f"Error fetching match IDs: {e}")
            return

        try:  # create MatchOverclass for match_id
            combined_match_data = MatchOverclass(most_recent_match_id)
            fig = combined_match_data.plot_gold_by_frame()
            st.pyplot(fig)
        except ValueError as ve:
            st.error(f"Value error occurred: {ve}")
        except TypeError as te:
            st.error(f"Type error occurred: {te}")
        except Exception as e:
            st.error(f"Unexpected error occurred: {e}")
            traceback_details = traceback.format_exc()
            st.error(f"Full traceback: {traceback_details}")


if __name__ == "__main__":
    main()
