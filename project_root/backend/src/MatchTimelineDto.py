import pandas as pd
from .api_client import API_Client
import json

class Metadata:
    def __init__(self, metadata_json):
        self.dataVersion = metadata_json['dataVersion']
        self.matchId = metadata_json['matchId']
        self.participants = metadata_json['participants']


class ChampionStats:
    def __init__(self, champ_stats_json):
        for key, value in champ_stats_json.items():
            setattr(self, key, value)


class DamageStats:
    def __init__(self, dmg_stats_json):
        for key, value in dmg_stats_json.items():
            setattr(self, key, value)


class ParticipantFrame:
    def __init__(self, p_frame_json):
        self.championStats = ChampionStats(p_frame_json['championStats'])
        self.damageStats = DamageStats(p_frame_json['damageStats'])
        self.currentGold = p_frame_json['currentGold']
        self.level = p_frame_json['level']
        self.totalGold = p_frame_json['totalGold']
        self.xp = p_frame_json['xp']


class Event:
    def __init__(self, event_json):
        for key, value in event_json.items():
            setattr(self, key, value)

class Frame:
    def __init__(self, frame_json):
        self.events = [Event(event) for event in frame_json['events']]
        self.participantFrames = {k: ParticipantFrame(v) for k, v in frame_json['participantFrames'].items()}
        self.timestamp = frame_json['timestamp']


class Info:
    def __init__(self, info_json):
        self.frameInterval = info_json['frameInterval']
        self.frames = [Frame(frame) for frame in info_json['frames']]
        self.gameId = info_json['gameId']
        self.participants = info_json['participants']


class MatchTimelineDto:
    def __init__(self, timeline_json):
        self.metadata = Metadata(timeline_json['metadata'])
        self.info = Info(timeline_json['info'])


    def get_gold_by_participant(self):
        # Initialize an empty list to store the data
        gold_data = []

        for frame in self.info.frames:
            timestamp = frame.timestamp
            # Iterate over each participant frame within a frame
            for participant_id, participant_frame in frame.participantFrames.items():
                # Extract the total gold for the participant in this frame
                total_gold = participant_frame.totalGold

                # Append the data to our list
                gold_data.append([timestamp, participant_id, total_gold])

        # Convert the list to a DataFrame
        gold_df = pd.DataFrame(gold_data, columns=["frame", "participant_id", "totalGold"])

        return gold_df


    def get_events_by_frame(self):
        event_data = []

        # Iterate over each frame
        for frame in self.info.frames:
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
    
    @staticmethod
    def get_match_timeline_dto(match_id):
        api_client = API_Client()
        match_timeline = api_client.get_match_timeline(match_id=match_id)
        return MatchTimelineDto(match_timeline.json())