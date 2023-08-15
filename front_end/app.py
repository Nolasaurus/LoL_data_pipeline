from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from src.get_match_ids_by_puuid import get_match_ids_by_puuid
from src.get_match_by_match_id import get_match_by_match_id
from src.extract_data_from_match import extract_data_from_match
from src.upload_matches import get_and_insert_match
from src.get_puuid_by_name import get_puuid_by_name
from src.extract_and_plot_gold_over_time import extract_gold_data, plot_gold_data
from src.connect_db import connect_db

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summoner', methods=['POST'])
def lookup():
    summoner_name = request.form['summoner_name'].strip()
    puuid = get_puuid_by_name(summoner_name)
    if puuid:
        match_ids = get_match_ids_by_puuid(puuid)
        matches_data = [get_match(match_id) for match_id in match_ids[:3]]
        return render_template('summoner.html', summoner_name=summoner_name, matches=matches_data)
    else:
        return "Summoner name not found or an error occurred", 400

def get_match(match_id):
    match_details_json, match_timeline_json = get_match_by_match_id(match_id)
    match_details_df = extract_data_from_match(match_details_json)
    match_details = match_details_df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
    # gold_data = extract_gold_data(match_id)
    # gold_chart_base64 = plot_gold_data(gold_data)

    return {
        "match_id": match_id,
        "details": match_details,
        # "gold_chart": gold_chart_base64,
        "columns": match_details_df.columns.tolist()
    }

# @app.route('/champion/<champion_id>')

# @app.route('/summoner/<summoner_name>')

if __name__ == '__main__':
    app.run(debug=True)
