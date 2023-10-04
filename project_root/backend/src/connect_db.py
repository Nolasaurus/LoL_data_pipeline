import psycopg2

def connect_db():
    with open('/home/nolan/projects/LoL_data_pipeline/postgres_pw.txt', 'r') as file:
        password = file.read().strip()
    return psycopg2.connect(
        dbname="loldb",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )