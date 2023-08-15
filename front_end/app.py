from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from src.get_match_ids_by_puuid import get_match_ids_by_puuid
from src.get_match_by_match_id import get_match_by_match_id
from src.extract_data_from_match import extract_data_from_match
from src.upload_matches import get_and_insert_match
from src.get_puuid_by_name import get_puuid_by_name
from src.extract_and_plot_gold_over_time import extract_gold_data, plot_gold_data
from src.connect_db import connect_db
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/lookup', methods=['POST'])
def lookup():
    print(request.form)  # Debugging line
    summoner_name = request.form['summoner_name'].strip()  # Get the summoner name from the form
    puuid = get_puuid_by_name(summoner_name)  # Translate the summoner name into a PUUID
    if puuid:
        match_ids = get_match_ids_by_puuid(puuid)
        return render_template('matches.html', puuid=puuid, match_ids=match_ids, summoner_name=summoner_name)
    else:
        return "Summoner name not found or an error occurred", 400

@app.route('/match/<match_id>')
def get_match(match_id):
    match_details_json, match_timeline_json = get_match_by_match_id(match_id)
    match_details_df = extract_data_from_match(match_details_json)
    match_details = match_details_df.to_records(index=False)
    gold_data = extract_gold_data(match_id)
    gold_chart_base64 = plot_gold_data(gold_data)

    return render_template('match.html', match_details=match_details, columns=match_details_df.columns, gold_chart_base64=gold_chart_base64)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summoner/<summoner_name>')
def summoner(summoner_name):
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to retrieve the last 3 matches for the given summoner
    query = """
        SELECT * FROM matches
        JOIN players ON matches.id = players.match_id
        WHERE players.summoner_name = %s
        LIMIT 3;
    """
    cursor.execute(query, (summoner_name,))
    matches = cursor.fetchall()

    # You'll need to process the results into a format that the template expects
    # ...

    return render_template('summoner.html', summoner_name=summoner_name, matches=matches)


# @app.route('/champion/<champion_id>')

# @app.route('/summoner/<summoner_name>')

if __name__ == '__main__':
    app.run(debug=True)
