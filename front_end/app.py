from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from src.get_match_ids_by_puuid import get_match_ids_by_puuid
from src.get_match_by_match_id import get_match_by_match_id
from src.extract_data_from_match import extract_data_from_match

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = "supersecretkey"  # Needed for flash messages

@app.route('/lookup', methods=['POST'])
def lookup():
    puuid = request.form['puuid']
    match_ids = get_match_ids_by_puuid(puuid)
    return render_template('matches.html', puuid=puuid, match_ids=match_ids)


@app.route('/match/<match_id>')
def get_match(match_id):
    match_details_json = get_match_by_match_id(match_id)
    match_details_df = extract_data_from_match(match_details_json)
    match_details = match_details_df.to_records(index=False)
    return render_template('match_data.html', match_details=match_details, columns=match_details_df.columns)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
