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

def execute_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
        connect_db().cursor.execute(sql_script)

def tables_exist(table_names):
    conn = connect_db()
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

# def _create_initial_tables():
#     # SQL file paths in the required order
#     sql_files = [
#         'sql_tables/match_metadata.sql',
#         'sql_tables/perks.sql',
#         'sql_tables/player_match_data.sql',
#         'sql_tables/challenges.sql',
#         'sql_tables/participant_frames.sql',
#         'sql_tables/match_events.sql',
#         'sql_tables/teams.sql'
#     ]

#     try:
#         conn = connect_db()
#         cursor = conn.cursor()
#         # Execute each SQL file
#         for file_path in sql_files:
#             execute_sql_file(file_path)
#             print(f"Executed {file_path}")

#         # Commit the changes
#         conn.commit()

#     except psycopg2.DatabaseError as e:
#         print(f"Database error: {e}")
#         if conn:
#             conn.rollback()

#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "execute_sql_file":
        execute_sql_file(sys.argv[2])