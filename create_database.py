import psycopg2
from psycopg2 import OperationalError
import getpass
import subprocess


def create_database(db_name, user, password, host='localhost', port='5432'):
    conn = None
    try:
        conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
        conn.autocommit = True

        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"Database {db_name} created successfully!")

    except OperationalError as e:
        print(f"The error '{e}' occurred")
    finally:
        if conn:
            cursor.close()
            conn.close()


def execute_sql_files_in_database(db_name, user, password, host='localhost', port='5432', sql_files=[]):
    for sql_file in sql_files:
        try:
            subprocess.run(
                ["psql", "-U", user, "-d", db_name, "-a", "-f", sql_file, "-h", host, "-p", str(port)],
                check=True,
                text=True,
                input=password
            )
            print(f"Executed {sql_file} in {db_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {sql_file} in {db_name}: {e}")


if __name__ == "__main__":
    DB_NAME = "test_task_6"

    USER = input("Please enter your PostgreSQL username: ")
    PASSWORD = getpass.getpass("Please enter your PostgreSQL password: ")

    HOST = "localhost"
    PORT = "5432"

    create_database(DB_NAME, USER, PASSWORD, HOST, PORT)

    sql_files = [
        "sql/create_table_cannabis_data.sql",
        "sql/create_table_nhl_team.sql",
        "sql/create_table_nhl_team_2.sql"
    ]
    execute_sql_files_in_database(DB_NAME, USER, PASSWORD, HOST, PORT, sql_files)
