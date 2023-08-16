from flask import Flask, render_template, request
from src.api_client import API_client
from src.extract_data_from_match import extract_data_from_match
from src.record_handler import RecordHandler, DatabaseConnectionError, DatabaseQueryError  # Import custom exceptions
from src.connect_db import connect_db

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
    except (DatabaseConnectionError, DatabaseQueryError) as e:
        app.logger.error(f"Error occurred: {e}")
        return "An error occurred while processing your request. Please try again later.", 500

def get_match(match_id):
    try:
        # Check the database first for match details
        match_details_json, match_timeline_json = record_handler.check_db_for_match(match_id)

        match_details_df = extract_data_from_match(match_details_json)
        match_details = match_details_df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries

        return {
            "match_id": match_id,
            "details": match_details,
            "columns": match_details_df.columns.tolist()
        }
    except (DatabaseConnectionError, DatabaseQueryError) as e:
        app.logger.error(f"Error occurred: {e}")
        return {
            "match_id": match_id,
            "details": [],
            "columns": []
        }

if __name__ == '__main__':
    app.run(debug=True)