import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def connect_db(user_role="readonly"):
    dbname = "loldb"
    user = (
        os.getenv("ADMIN_POSTGRES_USER")
        if user_role == "admin"
        else os.getenv("READONLY_POSTGRES_USER")
    )
    password = (
        os.getenv("ADMIN_POSTGRES_PASSWORD")
        if user_role == "admin"
        else os.getenv("READONLY_POSTGRES_PASSWORD")
    )
    host = "postgres"
    port = "5432"

    return psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )


def create_read_only_user(username, password):
    with connect_db("admin") as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE USER %s WITH PASSWORD %s;", (username, password))
            cursor.execute("GRANT CONNECT ON DATABASE loldb TO %s;", (username,))
            cursor.execute("GRANT USAGE ON SCHEMA public TO %s;", (username,))
            cursor.execute(
                "GRANT SELECT ON ALL TABLES IN SCHEMA public TO %s;", (username,)
            )
            cursor.execute(
                "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO %s;",
                (username,),
            )


def execute_sql_file(file_path):
    with open(file_path, "r") as file:
        sql_script = file.read()
        with connect_db("admin") as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_script)


def execute_sql_query(query):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                return False


def tables_exist(table_names):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            for table_name in table_names:
                cursor.execute(
                    "SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename = %s);",
                    (table_name,),
                )
                if not cursor.fetchone()[0]:
                    return False
            return True


def add_df_to_table(table_name, data_df):
    with connect_db() as conn:
        with conn.cursor("admin") as cursor:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
            db_columns = [desc[0] for desc in cursor.description]
            df_columns = data_df.columns.tolist()

            if db_columns != df_columns:
                print("Columns in df do not match cols in db table. Aborted.")
                return

            values = [tuple(row) for row in data_df.values]
            insert_stmt = f"INSERT INTO {table_name} ({','.join(df_columns)}) VALUES %s"
            psycopg2.extras.execute_values(cursor, insert_stmt, values)


def add_dict_to_table(table_name, data_dict):
    with connect_db("admin") as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
            db_columns = [desc[0] for desc in cursor.description]

            if set(db_columns) != set(data_dict.keys()):
                print("Keys in dict do not match cols in db table. Aborted.")
                return

            columns = ", ".join(data_dict.keys())
            placeholders = ", ".join(["%s"] * len(data_dict))
            insert_stmt = (
                f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            )
            cursor.execute(insert_stmt, list(data_dict.values()))


def _create_initial_tables():
    # SQL file paths in the required order
    sql_files = [
        "sql_tables/match_metadata.sql",
        "sql_tables/perks.sql",
        "sql_tables/player_match_data.sql",
        "sql_tables/challenges.sql",
        "sql_tables/participant_frames.sql",
        "sql_tables/match_events.sql",
        "sql_tables/teams.sql",
    ]

    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Execute each SQL file
        for file_path in sql_files:
            execute_sql_file(file_path)
            print(f"Executed {file_path}")

        # Commit the changes
        conn.commit()

    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
