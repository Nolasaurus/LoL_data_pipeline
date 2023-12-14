import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import contextlib
import logging
from typing import Dict

# Load environment variables
load_dotenv()

class SQLHelper:
    def __init__(self):
        pass

    @contextlib.contextmanager
    def db_connection(self, userrole="readonly"):
        conn = connect_db(userrole)  # Replace with actual connection logic
        try:
            yield conn
        except psycopg2.DatabaseError as e:
            logging.error("Database error: %s", e)
            conn.rollback()
            raise
        finally:
            conn.close()

    def insert_dict(self, table_name: str, data_dict: dict):
        try:
            with self.db_connection("admin") as conn:
                with conn.cursor() as cursor:
                    columns = ", ".join(data_dict.keys())
                    placeholders = ", ".join(["%s"] * len(data_dict))
                    values = tuple(data_dict.values())

                    insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    cursor.execute(insert_stmt, values)
                    conn.commit()
        except Exception as e:
            logging.error("Error in insert_dict: %s", e)
            raise

    def create_read_only_user(self, username, password):
        try:
            with self.db_connection() as conn:
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
        except Exception as e:
            logging.error("Error in create_read_only_user: %s", e)
            raise

    def execute_query(self, query, values=None, commit=True):
        try:
            with self.db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
                    if commit:
                        conn.commit()
                    else:
                        return cursor.fetchall()
        except Exception as e:
            logging.error("Error in execute_query: %s", e)
            raise


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
        dbname=dbname, user=user, password=password, host=host, port=port, connect_timeout=10
    )

def execute_sql_file(file_path):
    with open(file_path, "r") as file:
        sql_script = file.read()
        with connect_db("admin") as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_script)

def execute_batch_query(query, values_list, page_size=100):
    """
    Execute a batch SQL query using psycopg2's execute_values method.

    Args:
        query (str): The SQL query template to execute.
        values_list (list of tuple): A list of tuples, each containing the values to insert.
        page_size (int): Number of records to insert in a single batch.

    Returns:
        None
    """
    try:
        with connect_db("admin") as conn:
            with conn.cursor() as cursor:
                # Execute the batch query
                execute_values(cursor, query, values_list, page_size=page_size)
                # Commit the transaction
                conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        raise  # Re-raise the exception to be caught in the calling function

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
            execute_values(cursor, insert_stmt, values)
