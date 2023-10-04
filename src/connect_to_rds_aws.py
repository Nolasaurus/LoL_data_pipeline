import psycopg2
import boto3

def connect_to_rds(endpoint, port, user, region, dbname, profile_name='RDSCreds', sslcertificate="SSLCERTIFICATE"):
    """
    Connects to Amazon RDS PostgreSQL server.
    
    Args:
        endpoint (str): The RDS endpoint.
        port (str): Port number.
        user (str): Database username.
        region (str): AWS region.
        dbname (str): Name of the database.
        profile_name (str, optional): AWS profile name. Defaults to 'RDSCreds'.
        sslcertificate (str, optional): SSL Certificate path. Defaults to 'SSLCERTIFICATE'.

    Returns:
        psycopg2.extensions.connection: Connection object to the RDS PostgreSQL server.
    """
    # Gets the credentials from .aws/credentials
    print("Start boto3 session")
    session = boto3.Session(profile_name=profile_name)
    print("create client")
    client = session.client('rds')
    print("generate token")
    token = client.generate_db_auth_token(DBHostname=endpoint, Port=port, DBUsername=user, Region=region)
    
    try:
        print("start connection")
        conn = psycopg2.connect(host=endpoint, port=port, database=dbname, user=user, password=token, sslrootcert=sslcertificate)
        print("connection established")
        return conn
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return None


def execute_query(conn, query):
    """
    Executes a query on the provided database connection.

    Args:
        conn (psycopg2.extensions.connection): Connection object to the RDS PostgreSQL server.
        query (str): SQL query to execute.

    Returns:
        list: Results of the query.
    """
    try:
        print("Executing query")
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print("Query execution failed due to {}".format(e))
        return None