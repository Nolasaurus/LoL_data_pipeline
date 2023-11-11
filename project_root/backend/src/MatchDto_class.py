import json
import sys

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
    def __init__(self, statPerks: PerkStatsDto, styles: list[PerkStyleDto]):
        self.statPerks = statPerks
        self.styles = styles

class BanDto:
    def __init__(self, championId: int, pickTurn: int):
        self.championId = championId
        self.pickTurn = pickTurn

class ObjectiveDto:
    def __init__(self, first: bool, kills: int):
        self.first = first
        self.kills = kills

class ObjectivesDto:
    def __init__(self, baron: ObjectiveDto, champion: ObjectiveDto, dragon: ObjectiveDto, inhibitor: ObjectiveDto, riftHerald: ObjectiveDto, tower: ObjectiveDto):
        self.baron = baron
        self.champion = champion
        self.dragon = dragon
        self.inhibitor = inhibitor
        self.riftHerald = riftHerald
        self.tower = tower

class TeamDto:
    def __init__(self, bans: list[BanDto], objectives: ObjectivesDto, teamId: int, win: bool):
        self.bans = bans
        self.objectives = objectives
        self.teamId = teamId
        self.win = win

class ParticipantDto:
    def __init__(self, **kwargs):  # Using kwargs to simplify the example
        for key, value in kwargs.items():
            setattr(self, key, value)

class InfoDto:
    def __init__(self, gameCreation: int, gameDuration: int, gameEndTimestamp: int, gameId: int, gameMode: str, gameName: str, gameStartTimestamp: int, gameType: str, gameVersion: str, mapId: int, participants: list[ParticipantDto], platformId: str, queueId: int, teams: list[TeamDto], tournamentCode: str):
        self.gameCreation = gameCreation
        self.gameDuration = gameDuration
        self.gameEndTimestamp = gameEndTimestamp
        self.gameId = gameId
        self.gameMode = gameMode
        self.gameName = gameName
        self.gameStartTimestamp = gameStartTimestamp
        self.gameType = gameType
        self.gameVersion = gameVersion
        self.mapId = mapId
        self.participants = participants
        self.platformId = platformId
        self.queueId = queueId
        self.teams = teams
        self.tournamentCode = tournamentCode

class MetadataDto:
    def __init__(self, dataVersion: str, matchId: str, participants: list[str]):
        self.dataVersion = dataVersion
        self.matchId = matchId
        self.participants = participants

class MatchDto:
    def __init__(self, metadata: MetadataDto, info: InfoDto):
        self.match_id = metadata.matchId
        self.metadata = metadata
        self.info = info

    def to_dict(self):
        return {
            "metadata": vars(self.metadata),
            "info": vars(self.info)
        }

def create_objectives_dto(data):
    return ObjectivesDto(
        baron=ObjectiveDto(**data['baron']),
        champion=ObjectiveDto(**data['champion']),
        dragon=ObjectiveDto(**data['dragon']),
        inhibitor=ObjectiveDto(**data['inhibitor']),
        riftHerald=ObjectiveDto(**data['riftHerald']),
        tower=ObjectiveDto(**data['tower'])
    )

def create_team_dto(data):
    return TeamDto(
        bans=[BanDto(**ban) for ban in data['bans']],
        objectives=create_objectives_dto(data['objectives']),
        teamId=data['teamId'],
        win=data['win']
    )

def create_perks_dto(data):
    return PerksDto(
        statPerks=PerkStatsDto(**data['statPerks']),
        styles=[PerkStyleDto(description=style['description'],
                             selections=[PerkStyleSelectionDto(**selection) for selection in style['selections']],
                             style=style['style']) for style in data['styles']]
    )

def create_participant_dto(data):
    data['perks'] = create_perks_dto(data['perks'])
    return ParticipantDto(**data)

def create_info_dto(data):
    return InfoDto(
        gameCreation=data['gameCreation'],
        gameDuration=data['gameDuration'],
        gameEndTimestamp=data['gameEndTimestamp'],
        gameId=data['gameId'],
        gameMode=data['gameMode'],
        gameName=data['gameName'],
        gameStartTimestamp=data['gameStartTimestamp'],
        gameType=data['gameType'],
        gameVersion=data['gameVersion'],
        mapId=data['mapId'],
        participants=[create_participant_dto(participant) for participant in data['participants']],
        platformId=data['platformId'],
        queueId=data['queueId'],
        teams=[create_team_dto(team) for team in data['teams']],
        tournamentCode=data['tournamentCode']
    )

def parse_json_to_classes(json_data):
    data = json.loads(json_data)
    metadata = MetadataDto(**data['metadata'])
    info = create_info_dto(data['info'])
    return MatchDto(metadata, info)


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as file:
                match_json = file.read()
                match_dto_instance = parse_json_to_classes(match_json)
                print("Match DTO created successfully.")
                # You can add more logic here to use match_dto_instance
                print(match_dto_instance.to_dict())
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON file")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python script.py <path_to_match_json_file>")

if __name__ == "__main__":
    main()