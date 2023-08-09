from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = "supersecretkey"  # Needed for flash messages

def connect_db():
    with open('postgres_pw.txt', 'r') as file:
        password = file.read().strip()  # Reads the content and removes any leading/trailing whitespace
    return psycopg2.connect(
        dbname="loldb",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    puuid = request.form['puuid']
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM puuid WHERE puuid = %s", (puuid,))
    result = cursor.fetchall()
    connection.close()

    if result:
        # Here you can render another template with the result or handle it differently
        flash(f"Lookup successful: {result}")
    else:
        flash("PUUid not found.")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
