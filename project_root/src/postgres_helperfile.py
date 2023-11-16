import os
import psycopg2
from dotenv import load_dotenv


def connect_db():
    load_dotenv()
    return psycopg2.connect(
        dbname="loldb",
        user="nolan",
        password=os.environ.get("POSTGRES_PASSWORD"),
        host="localhost",
        port="5432",
    )


def create_table(table_name, columns):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS match (
                    match_id TEXT PRIMARY KEY,
                    match JSON NOT NULL,
                    match_timeline JSON
                );
                """
            )
            conn.commit()


def add_rows_to_table(table_name, data_df):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Retrieve the columns from the table in the database
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
        db_columns = [desc[0] for desc in cursor.description]

        # Get the columns from the DataFrame
        df_columns = data_df.columns.tolist()

        # Check if the columns match
        if db_columns != df_columns:
            print("Columns in df do not match cols in db table. Aborted.")
            return

        values = [tuple(row) for row in data_df.values]

        # Create the INSERT INTO statement
        insert_stmt = f"INSERT INTO {table_name} ({','.join(df_columns)}) VALUES %s"

        # Execute the insert
        psycopg2.extras.execute_values(cursor, insert_stmt, values)

        # Commit the transaction
        conn.commit()
    except Exception as e:
        # If any errors occur, rollback the transaction
        conn.rollback()
        print("An error occurred:", e)



