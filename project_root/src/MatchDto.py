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


class PerksDto:
    def __init__(self, data):
        self.statPerks = PerkStatsDto(data["statPerks"])
        self.styles = [PerkStyleDto(style) for style in data["styles"]]


class BanDto:
    def __init__(self, ban_json):
        self.championId = ban_json["championId"]
        self.pickTurn = ban_json["pickTurn"]


class ObjectiveDto:
    def __init__(self, objective_json):
        self.first = objective_json["first"]
        self.kills = objective_json["kills"]


class ObjectivesDto:
    def __init__(self, data):
        self.champion = ObjectiveDto(data["champion"])
        self.dragon = ObjectiveDto(data["dragon"])
        self.inhibitor = ObjectiveDto(data["inhibitor"])
        self.riftHerald = ObjectiveDto(data["riftHerald"])
        self.tower = ObjectiveDto(data["tower"])
        self.baron = ObjectiveDto(data["baron"])


class TeamDto:
    def __init__(self, data):
        self.bans = [BanDto(ban) for ban in data["bans"]]
        self.objectives = ObjectivesDto(data["objectives"])
        self.teamId = data["teamId"]
        self.win = data["win"]


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
                setattr(self, key, PerksDto(value))
            else:
                setattr(self, key, value)


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
        self.participants = [ParticipantDto(**p) for p in info["participants"]]
        self.platformId = info["platformId"]
        self.queueId = info["queueId"]
        self.teams = [TeamDto(t) for t in info["teams"]]
        self.tournamentCode = info.get("tournamentCode", "")


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
        self.metadata = MetadataDto(json["metadata"])
        self.match_id = self.metadata.matchId
        self.info = InfoDto(json["info"])


        
    def create_perks(self):
        '''
        Collates perk information into summary ready to insert into perks tables (see perks.sql)
        '''
        for participant in self.info.participants:
            participant_perks = participant['perks']

            # Extracting stat perks
            perk_stats = {
                'defense': participant_perks.statPerks.defense,
                'flex': participant_perks.statPerks.flex,
                'offense': participant_perks.statPerks.offense
            }

            # Assuming styles is a list and processing the first style as an example
            primary_style = participant_perks.styles[0]  # Adjust based on your needs
            perk_styles = {
                'description': primary_style.description,
                'style': primary_style.style
            }

        # Assuming selections is a list under primary_style
        perk_style_selections = []
        for selection in primary_style.selections:
            selection_data = {
                'perk': selection.perk,
                'var1': selection.var1,
                'var2': selection.var2,
                'var3': selection.var3
            }
            perk_style_selections.append(selection_data)

        return perk_stats, perk_styles, perk_style_selections
