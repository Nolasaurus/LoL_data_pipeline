import os
import psycopg2
import sys
from dotenv import load_dotenv


def connect_db():
    load_dotenv()
    return psycopg2.connect(
        dbname="loldb",
        user="nolan",
        password=os.environ.get("POSTGRES_PASSWORD"),
        host="postgres",
        port="5432",
    )


def tables_exist(conn, table_names):
    cursor = conn.cursor()
    try:
        for table_name in table_names:
            cursor.execute(f"SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename = '{table_name}');")
            print(cursor.fetchall)
            if not cursor.fetchone()[0]:
                return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()


def create_table_from_sql_file(sql_file_path, conn):
    # Connect to the database
    cursor = conn.cursor()

    # Read SQL from file
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Execute SQL script
    try:
        cursor.execute(sql_script)
        conn.commit()
        print("Table created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_tables_if_none():
    filepath = './sql_tables/'
    sql_files_to_table_names = {
        'match_metadata.sql': 'match_metadata',
        'perks.sql': 'perks',
        'player_match_data.sql': 'player_match_data',
        'challenges.sql': 'challenges',
        'participant_frames.sql': 'participant_frames',
        'match_events.sql': 'match_events'
    }

    # Connect to the database
    conn = connect_db()

    # Check if tables exist and create them if they don't
    for sql_file, table_name in sql_files_to_table_names.items():
        if not tables_exist(conn, [table_name]):
            create_table_from_sql_file(filepath + sql_file, conn)
            print(f'created table: {table_name}')

    # Close the database connection
    conn.close()


def add_df_to_table(table_name, data_df):
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


def add_dict_to_table(table_name, data_dict):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Retrieve the columns from the table in the database
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
        db_columns = [desc[0] for desc in cursor.description]

        # Check if the dictionary keys match the database columns
        if set(db_columns) != set(data_dict.keys()):
            print("Keys in dict do not match cols in db table. Aborted.")
            return

        # Create the INSERT INTO statement
        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join(['%s'] * len(data_dict))
        insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Execute the insert
        cursor.execute(insert_stmt, list(data_dict.values()))
        conn.commit()
        
    except Exception as e:
        # If any errors occur, rollback the transaction
        conn.rollback()
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "create_table_from_sql_file":
        create_table_from_sql_file(sys.argv[2])