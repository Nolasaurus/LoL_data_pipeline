import unittest
from unittest.mock import patch, MagicMock
import os
from postgres_helperfile import connect_db, SQLHelper

class TestConnectDB(unittest.TestCase):
    @patch('postgres_helperfile.psycopg2.connect')
    def test_connect_db_readonly(self, mock_connect):
        # Set environment variables for readonly user
        os.environ["READONLY_POSTGRES_USER"] = "readonly_user"
        os.environ["READONLY_POSTGRES_PASSWORD"] = "readonly_password"

        # Call the function
        conn = connect_db("readonly")

        # Assert that psycopg2.connect was called with the correct parameters, including the timeout
        mock_connect.assert_called_with(
            dbname="loldb", 
            user="readonly_user", 
            password="readonly_password", 
            host="postgres", 
            port="5432",
            connect_timeout=10  # Include the connect_timeout parameter in the assertion
        )

    @patch('postgres_helperfile.psycopg2.connect')
    def test_connect_db_admin(self, mock_connect):
        # Set environment variables for admin user
        os.environ["ADMIN_POSTGRES_USER"] = "admin_user"
        os.environ["ADMIN_POSTGRES_PASSWORD"] = "admin_password"

        # Call the function
        conn = connect_db("admin")

        # Assert that psycopg2.connect was called with the correct parameters, including the timeout
        mock_connect.assert_called_with(
            dbname="loldb", 
            user="admin_user", 
            password="admin_password", 
            host="postgres", 
            port="5432",
            connect_timeout=10
        )

class TestSQLHelper(unittest.TestCase):

    @patch('postgres_helperfile].connect_db')
    def test_insert_dict(self, mock_connect_db):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Instance of SQLHelper
        sql_helper = SQLHelper()

        # Sample data for testing
        table_name = 'test_table'
        data_dict = {'column1': 'value1', 'column2': 'value2'}

        # Call insert_dict method
        sql_helper.insert_dict(table_name, data_dict)

        # Check if the correct SQL statement is executed
        expected_query = 'INSERT INTO test_table (column1, column2) VALUES (%s, %s)'
        expected_values = tuple(data_dict.values())
        mock_cursor.execute.assert_called_once_with(expected_query, expected_values)

        # Check if commit is called
        mock_conn.commit.assert_called_once()
