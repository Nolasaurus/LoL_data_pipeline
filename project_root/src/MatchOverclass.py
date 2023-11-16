import matplotlib.pyplot as plt
from MatchDto import MatchDto
from MatchTimelineDto import MatchTimelineDto
from api_client import API_Client
import pandas as pd

class MatchOverclass:
    """
    Class to combine match data and match timeline for easier analysis and visualization.
    """

    def __init__(self, match_id):
        """
        Initializes the MatchOverclass with match data and timeline.

        Args: match_id

        match_data (MatchDto): Object containing the match data.
        match_timeline (MatchTimelineDto): Object containing the match timeline.
        """

        self.match_data = self.get_match_dto(match_id)
        self.match_timeline = self.get_match_timeline_dto(match_id)
        self.match_id = self.match_data.metadata.matchId
        self.puuid_dict = {participant.puuid: participant.summonerName for participant in self.match_data.info.participants}

    # def extract_match_summary(self):
    #     # extract from match_data game start, game duration, game type, teams, winning team
    #     game_start = self.match_data.info.gameStartTimestamp
    #     UTC_game_start = None # convert game_start to UTC

    #     game_duration = self.match_data.info.gameDuration
    #     game_len_hh_mm_ss = None # convert game_duration to hours, minutes, seconds
    #     # extract from match_timeline
    #     match_summary_df = None

    #     player_data = self.extract_player_data()
    #     # get KDA for each participant, gold and level, champion, total damage to champions
    #     return match_summary_df
    
    # def extract_player_data(self):
    #     # convert match_data.info.participants to a df. Challenges and perks should each be their own df
    #     ...


    def get_gold_by_summoner_name(self):
        # Initialize an empty list to store the data
        gold_data = []
        participant_dict = {}
        for participant in self.match_timeline.info.participants:
            participant_id = participant['participantId']
            puuid = participant['puuid']
            participant_dict[participant_id] = puuid

        for frame in self.match_timeline.info.frames:
            timestamp = frame.timestamp
            # Iterate over each participant frame within a frame
            for participant_id, participant_frame in frame.participantFrames.items():
                # Extract the total gold for the participant in this frame
                total_gold = participant_frame.totalGold

                # Append the data to our list
                puuid = participant_dict[int(participant_id)]
                summoner_name = self.puuid_dict[puuid]
                gold_data.append([timestamp, summoner_name, total_gold])

        # Convert the list to a DataFrame
        gold_df = pd.DataFrame(gold_data, columns=["frame", "summoner_name", "total_gold"])

        return gold_df


    def get_events_by_frame(self):
        event_data = []

        # Iterate over each frame
        for frame in self.match_timeline.info.frames:
            # Iterate over each event within a frame
            for event in frame.events:
                # Dictionary to hold event details
                event_details = {}

                # Dynamically add all properties of the event to the dictionary
                for key, value in event.__dict__.items():
                    event_details[key] = value

                # Append the event details to the event_data list
                event_data.append(event_details)

        # Convert the list of event details to a DataFrame
        event_df = pd.DataFrame(event_data)

        return event_df

    def plot_gold_by_frame(self) -> plt.Figure:
        gold_data = self.get_gold_by_summoner_name()

        fig, ax = plt.subplots(figsize=(10, 6))

        for summoner_name, group in gold_data.groupby('summoner_name'):
            ax.plot(group['frame'], group['total_gold'], label=summoner_name)

        ax.set_xlabel('Frame')
        ax.set_ylabel('Total Gold')
        ax.set_title(f'Total Gold Over Time for Match {self.match_id}')
        ax.legend()

        return fig
    
    @staticmethod
    def get_match_timeline_dto(match_id):
        api_client = API_Client()
        match_timeline = api_client.get_match_timeline(match_id)
        return MatchTimelineDto(match_timeline)
    
    @staticmethod
    def get_match_dto(match_id):
        api_client = API_Client()
        match_data = api_client.get_match_by_match_id(match_id)
        return MatchDto(match_data)
