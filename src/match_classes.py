import sys

def main(match_id):
    return MatchTimelineDto(match_id), MatchDto(match_id)

class MatchTimelineDto:
    def __init__(self, timeline_json):
        self.metadata = self.Metadata(timeline_json["metadata"])
        self.info = self.Info(timeline_json["info"])
        self.participants = self.metadata.participants

    class Metadata:
        def __init__(self, metadata_json):
            self.dataVersion = metadata_json["dataVersion"]
            self.matchId = metadata_json["matchId"]
            self.participants = metadata_json["participants"]

    class Info:
        def __init__(self, info_json):
            self.frameInterval = info_json["frameInterval"]
            self.frames = [self.Frame(frame) for frame in info_json["frames"]]
            self.gameId = info_json["gameId"]
            self.participants = info_json["participants"]

        class Frame:
            def __init__(self, frame_json):
                self.events = [self.Event(event) for event in frame_json["events"]]
                self.participantFrames = {
                    k: self.ParticipantFrame(v)
                    for k, v in frame_json["participantFrames"].items()
                }
                self.timestamp = frame_json["timestamp"]

            class Event:
                def __init__(self, event_json):
                    for key, value in event_json.items():
                        setattr(self, key, value)

            class ParticipantFrame:
                def __init__(self, p_frame_json):
                    self.championStats = self.ChampionStats(
                        p_frame_json["championStats"]
                    )
                    self.damageStats = self.DamageStats(p_frame_json["damageStats"])
                    self.currentGold = p_frame_json["currentGold"]
                    self.level = p_frame_json["level"]
                    self.totalGold = p_frame_json["totalGold"]
                    self.xp = p_frame_json["xp"]

                class ChampionStats:
                    def __init__(self, champ_stats_json):
                        for key, value in champ_stats_json.items():
                            setattr(self, key, value)

                class DamageStats:
                    def __init__(self, dmg_stats_json):
                        for key, value in dmg_stats_json.items():
                            setattr(self, key, value)



class MatchDto:
    """
    Represents a match data transfer object, encapsulating all relevant information about a match.

    This class serves as a high-level container for match data, including metadata and detailed
    information about the game and its participants.

    Attributes:
        metadata (MetadataDto): An object containing basic metadata about the match, such as version,
                                match ID, and participant IDs.
        match_id (str): The unique identifier of the match derived from the metadata.
        info (InfoDto): An object containing detailed information about the game, including game settings,
                        participant details, team compositions, and game-specific statistics.

    Args:
        json (dict): A dictionary containing match data, with keys 'metadata' and 'info'.
                     The 'metadata' key should map to a dictionary suitable for initializing MetadataDto,
                     and the 'info' key should map to a dictionary suitable for initializing InfoDto.
    """

    def __init__(self, json):
        print("MatchDto called")
        self.metadata = self.MetadataDto(json["metadata"])
        self.match_id = self.metadata.matchId
        self.info = self.InfoDto(json["info"])

        print(self.metadata, self.info)

    class MetadataDto:
        """
        Represents the metadata for a match, including data version, match ID, and participant identifiers.

        Attributes:
            dataVersion (str): Version of the data format.
            matchId (str): Unique identifier of the match.
            participants (list[str]): List of participant identifiers.
        """

        def __init__(self, metadata):
            self.dataVersion = metadata["dataVersion"]
            self.matchId = metadata["matchId"]
            self.participants = metadata["participants"]

    class InfoDto:
        """
        Contains detailed information about the match, including game settings and participant details.
        """

        def __init__(self, info):
            self.gameCreation = info["gameCreation"]
            self.gameDuration = info["gameDuration"]
            self.gameEndTimestamp = info["gameEndTimestamp"]
            self.gameId = info["gameId"]
            self.gameMode = info["gameMode"]
            self.gameName = info["gameName"]
            self.gameStartTimestamp = info["gameStartTimestamp"]
            self.gameType = info["gameType"]
            self.gameVersion = info["gameVersion"]
            self.mapId = info["mapId"]
            self.participants = [self.ParticipantDto(**p) for p in info["participants"]]
            self.platformId = info["platformId"]
            self.queueId = info["queueId"]
            self.teams = [self.TeamDto(t) for t in info["teams"]]
            self.tournamentCode = info.get("tournamentCode", "")

        class ParticipantDto:
            """
            Represents detailed information about an individual participant in the game.
            Attributes:
                Various attributes representing participant's performance in the game, such as
                participantId, championId, championName, teamId, kills, deaths, assists, totalDamageDealt,
                goldEarned, and many others.
            """

            def __init__(self, **kwargs):
                for key, value in kwargs.items():
                    if key == "perks":
                        setattr(self, key, self.PerksDto(value))
                    else:
                        setattr(self, key, value)

            class PerksDto:
                def __init__(self, data):
                    self.statPerks = self.PerkStatsDto(data["statPerks"])
                    self.styles = [self.PerkStyleDto(style) for style in data["styles"]]

                class PerkStatsDto:
                    def __init__(self, perk_stats_json):
                        self.defense = perk_stats_json["defense"]
                        self.flex = perk_stats_json["flex"]
                        self.offense = perk_stats_json["offense"]

                class PerkStyleSelectionDto:
                    def __init__(self, perk_selection_json):
                        self.perk = perk_selection_json["perk"]
                        self.var1 = perk_selection_json["var1"]
                        self.var2 = perk_selection_json["var2"]
                        self.var3 = perk_selection_json["var3"]

                class PerkStyleDto:
                    def __init__(self, perk_style_json):
                        self.description = perk_style_json["description"]
                        self.selections = perk_style_json["selections"]
                        self.style = perk_style_json["style"]

        class TeamDto:
            def __init__(self, data):
                self.bans = [self.BanDto(ban) for ban in data["bans"]]
                self.objectives = self.ObjectivesDto(data["objectives"])
                self.teamId = data["teamId"]
                self.win = data["win"]

            class ObjectivesDto:
                def __init__(self, data):
                    self.objectives = {}  # Dictionary to store ObjectiveDto instances
                    for objective_name in [
                        "champion",
                        "dragon",
                        "inhibitor",
                        "riftHerald",
                        "tower",
                        "baron",
                    ]:
                        if objective_name in data:
                            self.objectives[objective_name] = self.ObjectiveDto(
                                data[objective_name]
                            )

                class ObjectiveDto:
                    def __init__(self, objective_json):
                        self.first = objective_json.get(
                            "first", False
                        )  # Default to False if not present
                        self.kills = objective_json.get(
                            "kills", 0
                        )  # Default to 0 if not present

                def get_objective(self, name):
                    """Returns the ObjectiveDto for the given name, or None if not found."""
                    return self.objectives.get(name)

            class BanDto:
                def __init__(self, ban_json):
                    self.championId = ban_json["championId"]
                    self.pickTurn = ban_json["pickTurn"]

    def create_perks(self):
        """
        Collates perk information into summary ready to insert into perks tables (see perks.sql)
        """
        for participant in self.info.participants:
            participant_perks = participant["perks"]

            # Extracting stat perks
            perk_stats = {
                "defense": participant_perks.statPerks.defense,
                "flex": participant_perks.statPerks.flex,
                "offense": participant_perks.statPerks.offense,
            }

            # Assuming styles is a list and processing the first style as an example
            primary_style = participant_perks.styles[0]  # Adjust based on your needs
            perk_styles = {
                "description": primary_style.description,
                "style": primary_style.style,
            }

        # Assuming selections is a list under primary_style
        perk_style_selections = []
        for selection in primary_style.selections:
            selection_data = {
                "perk": selection.perk,
                "var1": selection.var1,
                "var2": selection.var2,
                "var3": selection.var3,
            }
            perk_style_selections.append(selection_data)

        return perk_stats, perk_styles, perk_style_selections


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])



if __name__ == "__main__":
    # if 2nd arg is match_id
    if len(sys.argv) == 2:
        main(sys.argv[1])
