class PerkStatsDto:
    def __init__(self, defense: int, flex: int, offense: int):
        self.defense = defense
        self.flex = flex
        self.offense = offense

class PerkStyleSelectionDto:
    def __init__(self, perk: int, var1: int, var2: int, var3: int):
        self.perk = perk
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

class PerkStyleDto:
    def __init__(self, description: str, selections: list[PerkStyleSelectionDto], style: int):
        self.description = description
        self.selections = selections
        self.style = style

class PerksDto:
    def __init__(self, data):
        self.statPerks = PerkStatsDto(**data['statPerks'])
        self.styles = [PerkStyleDto(description=style['description'],
                                    selections=[PerkStyleSelectionDto(**selection) for selection in style['selections']],
                                    style=style['style']) for style in data['styles']]

class BanDto:
    def __init__(self, championId: int, pickTurn: int):
        self.championId = championId
        self.pickTurn = pickTurn

class ObjectiveDto:
    def __init__(self, first: bool, kills: int):
        self.first = first
        self.kills = kills


class ObjectivesDto:
    def __init__(self, data):
        self.champion=ObjectiveDto(**data['champion'])
        self.dragon=ObjectiveDto(**data['dragon'])
        self.inhibitor=ObjectiveDto(**data['inhibitor'])
        self.riftHerald=ObjectiveDto(**data['riftHerald'])
        self.tower=ObjectiveDto(**data['tower'])
        self.baron = ObjectiveDto(**data['baron'])



class TeamDto:
    def __init__(self, data):
        self.bans = [BanDto(**ban) for ban in data['bans']]
        self.objectives = ObjectivesDto(data['objectives'])
        self.teamId = data['teamId']
        self.win = data['win']


class ParticipantDto:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'perks':
                setattr(self, key, PerksDto(value))
            else:
                setattr(self, key, value)


class InfoDto:
    def __init__(self, info):
        self.gameCreation = info.gameCreation
        self.gameDuration = info.gameDuration
        self.gameEndTimestamp = info.gameEndTimestamp
        self.gameId = info.gameId
        self.gameMode = info.gameMode
        self.gameName = info.gameName
        self.gameStartTimestamp = info.gameStartTimestamp
        self.gameType = info.gameType
        self.gameVersion = info.gameVersion
        self.mapId = info.mapId
        self.participants = info.participants
        self.platformId = info.platformId
        self.queueId = info.queueId
        self.teams = info.teams
        self.tournamentCode = info.tournamentCode

class MetadataDto:
    def __init__(self, metadata):
        self.dataVersion = metadata['dataVersion']
        self.matchId = metadata['matchId']
        self.participants = metadata['participants']

class MatchDto:
    def __init__(self, json):
        self.metadata = MetadataDto(**json.metadata)
        self.match_id = json.metadata.matchId
        self.info = InfoDto(**json.info)
