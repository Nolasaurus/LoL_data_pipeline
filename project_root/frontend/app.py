from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summoner', methods=['POST'])
def lookup():
    summoner_name = request.form['summoner_name'].strip()
    summoner_data = get_summoner_data(summoner_name)


def get_summoner_data(summoner_name):
    # connect to psql docker
    # 


if __name__ == '__main__':
    app.run(debug=True)
