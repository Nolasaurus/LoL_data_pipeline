from .api_client import API_Client
import json

'''
Class and Sub-Class Structure:

MatchDto
    MetadataDto
    InfoDto
        ParticipantDto
            PerksDto
                PerkStatsDto
                PerkStyleDto
                    PerkStyleSelectionDto
        TeamDto
            BanDto
            ObjectivesDto
                ObjectiveDto
'''

class PerkStatsDto:
    def __init__(self, perk_stats_json):
        self.defense = perk_stats_json['defense']
        self.flex = perk_stats_json['flex']
        self.offense = perk_stats_json['offense']


class PerkStyleSelectionDto:
    def __init__(self, perk_selection_json):
        self.perk = perk_selection_json['perk']
        self.var1 = perk_selection_json['var1']
        self.var2 = perk_selection_json['var2']
        self.var3 = perk_selection_json['var3']


class PerkStyleDto:
    def __init__(self, perk_style_json):
        self.description = perk_style_json['description']
        self.selections = perk_style_json['selections']
        self.style = perk_style_json['style']


class PerksDto:
    def __init__(self, data):
        self.statPerks = PerkStatsDto(data['statPerks'])
        self.styles = [PerkStyleDto(style) for style in data['styles']]


class BanDto:
    def __init__(self, ban_json):
        self.championId = ban_json['championId']
        self.pickTurn = ban_json['pickTurn']


class ObjectiveDto:
    def __init__(self, objective_json):
        self.first = objective_json['first']
        self.kills = objective_json['kills']


class ObjectivesDto:
    def __init__(self, data):
        self.champion=ObjectiveDto(data['champion'])
        self.dragon=ObjectiveDto(data['dragon'])
        self.inhibitor=ObjectiveDto(data['inhibitor'])
        self.riftHerald=ObjectiveDto(data['riftHerald'])
        self.tower=ObjectiveDto(data['tower'])
        self.baron = ObjectiveDto(data['baron'])


class TeamDto:
    def __init__(self, data):
        self.bans = [BanDto(ban) for ban in data['bans']]
        self.objectives = ObjectivesDto(data['objectives'])
        self.teamId = data['teamId']
        self.win = data['win']


class ParticipantDto:
    '''
    Represents detailed information about an individual participant in the game.
    Attributes:
        Various attributes representing participant's performance in the game, such as
        participantId, championId, championName, teamId, kills, deaths, assists, totalDamageDealt,
        goldEarned, and many others.
    '''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'perks':
                setattr(self, key, PerksDto(value))
            else:
                setattr(self, key, value)


class InfoDto:
    """
    Contains detailed information about the match, including game settings and participant details.
    """
    def __init__(self, info):
        self.gameCreation = info['gameCreation']
        self.gameDuration = info['gameDuration']
        self.gameEndTimestamp = info['gameEndTimestamp']
        self.gameId = info['gameId']
        self.gameMode = info['gameMode']
        self.gameName = info['gameName']
        self.gameStartTimestamp = info['gameStartTimestamp']
        self.gameType = info['gameType']
        self.gameVersion = info['gameVersion']
        self.mapId = info['mapId']
        self.participants = [ParticipantDto(**p) for p in info['participants']]
        self.platformId = info['platformId']
        self.queueId = info['queueId']
        self.teams = [TeamDto(t) for t in info['teams']]
        self.tournamentCode = info.get('tournamentCode', '')



class MetadataDto:
    """
    Represents the metadata for a match, including data version, match ID, and participant identifiers.
    
    Attributes:
        dataVersion (str): Version of the data format.
        matchId (str): Unique identifier of the match.
        participants (list[str]): List of participant identifiers.
    """

    def __init__(self, metadata):
        self.dataVersion = metadata['dataVersion']
        self.matchId = metadata['matchId']
        self.participants = metadata['participants']


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
        self.metadata = MetadataDto(json['metadata'])
        self.match_id = self.metadata.matchId
        self.info = InfoDto(json['info'])

    @staticmethod
    def get_match_dto(match_id):
        api_client = API_Client()
        match_data = api_client.get_match_by_match_id(match_id=match_id)
        return MatchDto(match_data.json())



