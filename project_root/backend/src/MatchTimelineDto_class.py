import json
import sys
import pandas as pd

class Metadata:
    def __init__(self, dataVersion, matchId, participants):
        self.dataVersion = dataVersion
        self.matchId = matchId
        self.participants = participants


class ChampionStats:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class DamageStats:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class ParticipantFrame:
    def __init__(self, **kwargs):
        self.championStats = ChampionStats(**kwargs.get('championStats', {}))
        self.damageStats = DamageStats(**kwargs.get('damageStats', {}))
        self.currentGold = kwargs.get('currentGold', 0)
        self.level = kwargs.get('level', 0)
        self.totalGold = kwargs.get('totalGold', 0)
        self.xp = kwargs.get('xp', 0)
        # Add more properties as needed


class Event:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Frame:
    def __init__(self, events, participantFrames, timestamp):
        self.events = [Event(**event) for event in events]
        self.participantFrames = {k: ParticipantFrame(**v) for k, v in participantFrames.items()}
        self.timestamp = timestamp


class Info:
    def __init__(self, frameInterval, frames, gameId, participants):
        self.frameInterval = frameInterval
        self.frames = [Frame(**frame) for frame in frames]
        self.gameId = gameId
        self.participants = participants


class MatchTimelineDto:
    def __init__(self, metadata, info):
        self.metadata = Metadata(**metadata)
        self.info = Info(**info)

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