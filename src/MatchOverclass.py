import postgres_helperfile
from MatchDto import MatchDto
from MatchTimelineDto import MatchTimelineDto
from api_client import API_Client

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

        self.match_data = self.get_match_dto(match_id, API_Client)
        self.match_timeline = self.get_match_timeline_dto(match_id, API_Client)
        self.match_id = self.match_data.metadata.matchId
        self.puuid_dict = {
            participant.puuid: participant.summonerName
            for participant in self.match_data.info.participants
        }

    def insert_match_metadata(self):
        '''
        Collate MatchDto information into summary and insert into table match_metadata (see match_metadata.sql)
        '''

        conn = postgres_helperfile.connect_db()
        cursor = conn.cursor()

        try:
            # Check if match_id already exists in the table
            cursor.execute("SELECT COUNT(*) FROM match_metadata WHERE matchId = %s", (self.match_data.metadata.matchId,))
            if cursor.fetchone()[0] == 0:
                # The match_id does not exist, proceed with insertion
                match_metadata_dict = {
                    'dataVersion': self.match_data.metadata.dataVersion,
                    'matchId': self.match_data.metadata.matchId,
                    'gameCreation': self.match_data.info.gameCreation,
                    'gameDuration': self.match_data.info.gameDuration,
                    'gameEndTimestamp': self.match_data.info.gameEndTimestamp,
                    'gameId': self.match_data.info.gameId,
                    'gameMode': self.match_data.info.gameMode,
                    'gameName': self.match_data.info.gameName,
                    'gameStartTimestamp': self.match_data.info.gameStartTimestamp,
                    'gameType': self.match_data.info.gameType,
                    'gameVersion': self.match_data.info.gameVersion,
                    'mapId': self.match_data.info.mapId,
                    'platformId': self.match_data.info.platformId,
                    'queueId': self.match_data.info.queueId,
                    'tournamentCode': self.match_data.info.tournamentCode
                }

                postgres_helperfile.add_dict_to_table('match_metadata', match_metadata_dict)
            else:
                print("Match with this ID already exists in the database.")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            cursor.close()
            conn.close()


    def push_data_to_sql(self):
        self.insert_match_metadata


    @staticmethod
    def get_match_timeline_dto(match_id, api_client):
        match_timeline = api_client.get_match_timeline(match_id)
        return MatchTimelineDto(match_timeline)

    @staticmethod
    def get_match_dto(match_id, api_client):
        match_data = api_client.get_match_by_match_id(match_id)
        return MatchDto(match_data)
