from flask import Flask, render_template, request
from src.api_client import API_client
from src.extract_data_from_match import extract_data_from_match

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summoner', methods=['POST'])
def lookup():
    summoner_name = request.form['summoner_name'].strip()
    puuid = API_client().get_puuid_by_name(summoner_name)
    if puuid:
        match_ids = API_client().get_match_ids_by_puuid(puuid)
        matches_data = [get_match(match_id) for match_id in match_ids[:3]]
        return render_template('summoner.html', summoner_name=summoner_name, matches=matches_data)
    else:
        return "Summoner name not found or an error occurred", 400

def get_match(match_id):
    match_details_json = API_client().get_match_by_match_id(match_id)
    match_details_df = extract_data_from_match(match_details_json)
    match_details = match_details_df.to_dict(orient='records')  # Convert df to list of dicts

    return {
        "match_id": match_id,
        "details": match_details,
        "columns": match_details_df.columns.tolist()
    }

if __name__ == '__main__':
    app.run(debug=True)