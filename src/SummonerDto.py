from api_client import API_Client

class SummonerDto:
    def __init__(self, json):
        self.account_id = json.get("accountId")
        self.profile_icon_id = json.get("profileIconId")
        self.revision_date = json.get("revisionDate")
        self.name = json.get("name")
        self.id = json.get("id")
        self.puuid = json.get("puuid")
        self.summoner_level = json.get("summonerLevel")

    @staticmethod
    def get_summoner_dto(summoner_name):
        api_client = API_Client()
        try:
            summoner_data = api_client.get_summoner_by_name(summoner_name)
            if summoner_data:
                return SummonerDto(summoner_data)
            else:
                raise ValueError("No data returned for summoner")
        except Exception as e:
            raise Exception(f"Failed to get summoner data: {e}")
