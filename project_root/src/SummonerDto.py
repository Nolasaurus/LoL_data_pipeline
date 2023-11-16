from api_client import API_Client

class SummonerDto:
    def __init__(self, json):
        self.account_id = json['accountId']
        self.profile_icon_id = json['profileIconId']
        self.revision_date = json['revisionDate']
        self.name = json['name']
        self.id = json['id']
        self.puuid = json['puuid']
        self.summoner_level = json['summonerLevel']

    @staticmethod
    def get_summoner_dto(summoner_name):
        api_client = API_Client()
        summoner_data = api_client.get_summoner_by_name(summoner_name)
        return SummonerDto(summoner_data)



