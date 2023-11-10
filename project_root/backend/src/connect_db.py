import os
import psycopg2
from dotenv import load_dotenv

def connect_db():
    load_dotenv()
    return psycopg2.connect(
        dbname="loldb",
        user="nolan",
        password= os.environ.get("POSTGRES_PASSWORD"),
        host="localhost",
        port="5432"
    )