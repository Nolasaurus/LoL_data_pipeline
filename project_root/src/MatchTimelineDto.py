class Metadata:
    def __init__(self, metadata_json):
        self.dataVersion = metadata_json["dataVersion"]
        self.matchId = metadata_json["matchId"]
        self.participants = metadata_json["participants"]


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
        self.championStats = ChampionStats(p_frame_json["championStats"])
        self.damageStats = DamageStats(p_frame_json["damageStats"])
        self.currentGold = p_frame_json["currentGold"]
        self.level = p_frame_json["level"]
        self.totalGold = p_frame_json["totalGold"]
        self.xp = p_frame_json["xp"]


class Event:
    def __init__(self, event_json):
        for key, value in event_json.items():
            setattr(self, key, value)


class Frame:
    def __init__(self, frame_json):
        self.events = [Event(event) for event in frame_json["events"]]
        self.participantFrames = {
            k: ParticipantFrame(v) for k, v in frame_json["participantFrames"].items()
        }
        self.timestamp = frame_json["timestamp"]


class Info:
    def __init__(self, info_json):
        self.frameInterval = info_json["frameInterval"]
        self.frames = [Frame(frame) for frame in info_json["frames"]]
        self.gameId = info_json["gameId"]
        self.participants = info_json["participants"]


class MatchTimelineDto:
    def __init__(self, timeline_json):
        self.metadata = Metadata(timeline_json["metadata"])
        self.info = Info(timeline_json["info"])
        self.participants = self.metadata.participants
