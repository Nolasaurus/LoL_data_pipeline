import pandas as pd
import psycopg2.extras
from connect_db import connect_db

class DataProcessor:
    @staticmethod
    def check_if_data_in_db(table_name, data_df, unique_columns):
        conn = connect_db()
        cursor = conn.cursor()
        try:
            # Construct the WHERE clause based on unique_columns
            where_clause = ' OR '.join([f"{col} = %s" for col in unique_columns])

            for index, row in data_df.iterrows():
                unique_values = [row[col] for col in unique_columns]
                query = f"SELECT * FROM {table_name} WHERE {where_clause}"
                cursor.execute(query, unique_values)

                # If any row is found, the data is already in the database
                if cursor.fetchone():
                    return True

            return False
        except Exception as e:
            print("An error occurred:", e)
            return False

    @staticmethod
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

    @staticmethod
    def process_match(raw_match_json):
        participant_match_details = raw_match_json['info']['participants']
        participant_match_details_df = pd.DataFrame(participant_match_details)
        table_name = 'player_match_stats'
        DataProcessor.add_rows_to_table(table_name, participant_match_details_df)

    # @staticmethod
    # def process_match_timeline(raw_match_timeline_json):
    #     # Extract data from raw_match_timeline_json into a DataFrame
    #     timeline_details_df = # Code to create DataFrame from raw_match_timeline_json

    #     table_name = 'match_timeline'
    #     # Use the add_rows_to_table function to insert the data
    #     DataProcessor.add_rows_to_table(table_name, timeline_details_df)
