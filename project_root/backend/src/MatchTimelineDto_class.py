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

        # Iterate over each frame
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

def to_dict(obj):
    """
    Helper function to recursively convert an object to a dictionary.
    """
    if isinstance(obj, list):
        return [to_dict(e) for e in obj]
    elif isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}
    elif hasattr(obj, "__dict__"):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}
    else:
        return obj
    

def create_MatchTimelineDto_instance(timeline_json):
    return MatchTimelineDto(timeline_json['metadata'], timeline_json['info'])


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as file:
                timeline_data = json.load(file)
                return MatchTimelineDto(timeline_data['metadata'], timeline_data['info'])
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON file")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python script.py <path_to_match_timeline_json_file>")

if __name__ == "__main__":
    main()