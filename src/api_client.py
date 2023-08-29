import requests
import json
import boto3
from src.get_API_key import get_API_key

class APIKeyExpiredError(Exception):
    pass

class API_client:
    def __init__(self):
        self.api_key = get_API_key()
        self.s3_client = None  # Initialize the s3_client attribute as None
        self.bucket_name = 'lol-api-bucket'
        self.role_arn = 'arn:aws:iam::626950961975:role/lol-s3'

    def store_to_s3(self, filename, data):
        sts_client = boto3.client('sts')  # Initialize the STS client
        assumed_role = sts_client.assume_role(
            RoleArn=self.role_arn,
            RoleSessionName='S3UploadSession'
        )
        credentials = assumed_role['Credentials']
        
        # Initialize the S3 client with the temporary credentials
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        )

        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=json.dumps(data),
                ContentType='application/json'
            )
        except Exception as e:
            print(f"Error uploading to S3: {e}")
    
    def _make_request(self, url, timeout=None):
        # Common code to make an HTTP request to the API
        try:
            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                raise APIKeyExpiredError("Riot API key expired")
            else:
                print(f"Error: {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            print(f"Request timed out for url: {url}")
            return None

    def get_puuid_by_name(self, summoner_name):
        summoner_name_encoded = summoner_name.strip().replace(" ", "%20") # Remove leading/trailing whitespaces and encode space character
        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}?api_key={self.api_key}'
        response = self._make_request(url, timeout=5)
        return response['puuid'] if response else None

    def get_match_ids_by_puuid(self, puu_id, start=0, count=20):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={start}&count={count}&api_key={self.api_key}'
        return self._make_request(url, timeout=5)

    def get_match_by_match_id(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}'
        response = self._make_request(url, timeout=5)
        if response:
            self.store_to_s3(f"matches/{match_id}.json", response)
            return response
    
    def get_match_timeline(self, match_id):
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={self.api_key}'
        response = self._make_request(url, timeout=5)
        if response:
            self.store_to_s3(f"match_timelines/{match_id}.json", response)
            return response

    def get_puuid_by_summon_id(self, summoner_id):
        url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={self.api_key}'
        response = self._make_request(url, timeout=5)
        return response['puuid'] if response else None
    
    def get_summoner_ids_from_league_id(self, league_id):
        url = f'https://na1.api.riotgames.com/lol/league/v4/leagues/{league_id}?api_key={self.api_key}'
        response = self._make_request(url, timeout=5)
        if response:
            summoner_ids = [entry['summonerId'] for entry in response['entries']]
            return summoner_ids
        else:
            return None

