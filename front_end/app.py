from flask import Flask, render_template, request
from src.api_client import API_client, APIKeyExpiredError
from src.record_handler import RecordHandler
import pandas as pd

app = Flask(__name__, static_url_path='', static_folder='static')
api_client = API_client()
record_handler = RecordHandler()  # Create an instance of the RecordHandler class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summoner', methods=['POST'])
def lookup():
    summoner_name = request.form['summoner_name'].strip()
    
    try:
        # Check the database first for the puuid
        puuid = record_handler.check_db_for_summoner_name(summoner_name)
        
        if puuid:
            # Check the database for match_ids associated with the puuid
            match_ids = record_handler.check_db_for_match_ids(puuid)
            matches_data = [get_match(match_id) for match_id in match_ids[:3]]
            return render_template('summoner.html', summoner_name=summoner_name, matches=matches_data)
        else:
            return "Summoner name not found or an error occurred", 400
    except APIKeyExpiredError:
        return "API key expired", 403
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return "An error occurred while processing your request. Please try again later.", 500


def extract_data_from_match(match_data):
    metadata = match_data['metadata']
    info = match_data['info']
    match_id = metadata['matchId']
    game_duration = info['gameDuration']

    included_fields = pd.read_csv('/home/nolan/projects/LoL_data_pipeline/included_match_fields.csv')
    included_fields_list = included_fields.iloc[:, 0].tolist()    
    
    data = pd.DataFrame(info['participants'])[included_fields_list]
    # data.insert(0, 'PUUid', metadata['participants'])
    # data.insert(0, 'match_id', match_id)
    
    return data    

def get_match(match_id):
    match_details_json = API_client().get_match_by_match_id(match_id)
    match_details_df = extract_data_from_match(match_details_json)
    # Convert df to list of dicts
    match_details = match_details_df.to_dict(orient='records')  

    match_details_df = extract_data_from_match(match_details_json)
    match_details = match_details_df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries

    return {
        "match_id": match_id,
        "details": match_details,
        "columns": match_details_df.columns.tolist()
    }
def extract_events_from_timeline(match_timeline):
    game_event_df = pd.DataFrame()
    # TODO implement pFrames
    # game_pFrames_df = pd.DataFrame()
    for i, frame in enumerate(match_timeline['info']['frames']):
        events = pd.DataFrame(match_timeline['info']['frames'][i]['events'])
        # TODO 
        # pFrames = pd.DataFrame(match_timeline['info']['frames'][i]['participantFrames'])

        # concat events to game_event_df
        game_event_df = pd.concat([game_event_df, events], ignore_index=True)
        
        # game_pFrames_df = pd.concat([game_pFrames_df, pFrames], ignore_index=True)

    return game_event_df #, game_pFrames_df

if __name__ == '__main__':
    app.run(debug=True)
