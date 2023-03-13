import pandas as pd
import psycopg2
from config import DB_DETAILS
from mysql import connector as mc
from mysql.connector import errorcode as ec


def load_db_details(env):
    return DB_DETAILS(env)


def get_pg_connection(db_host, db_name, db_user, db_pass):
    connection = psycopg2.connect(
        f"dbname={db_name} host={db_host} user={db_user} password={db_pass}"
    )
    return connection


def get_mysql_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mc.connect(
            user=db_user,
            password=db_pass,
            host=db_host,
            database=db_name
        )

    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        elif error.errno == ec.ER_PROCACCESS_DENIED_ERROR:
            print("Access denied for the user")
        else:
            print(error)

    return connection


def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None

    if db_type == 'mysql':
        connection = get_mysql_connection(
            db_user=db_user,
            db_pass=db_pass,
            db_host=db_host,
            db_name=db_name
        )

    if db_type == 'postgres':
        connection = get_pg_connection(
            db_user=db_user,
            db_pass=db_pass,
            db_host=db_host,
            db_name=db_name
        )

    return connection


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_load == "yes"')

