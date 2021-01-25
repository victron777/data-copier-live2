from mysql import connector as mc
from mysql.connector import errorcode as ec
import psycopg2
import pandas as pd
from config import DB_DETAILS


def load_db_details(env):
    return DB_DETAILS[env]


def get_mysql_connection(db_host, db_port, db_name, db_user, db_pass):
    connection = mc.connect()
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                port=db_port,
                                database=db_name)
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)
    return connection


def get_pg_connection(db_host, db_name, db_user, db_pass, db_port):
    connection = psycopg2.connect("dbname={} user={} host={} password={} port={}"
                                  .format(db_name, db_user, db_host, db_pass, db_port))
    return connection


def get_connection(db_type, db_host, db_port, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_port=db_port,
                                          db_name=db_name,
                                          db_user=db_user,
                                          db_pass=db_pass)
    if db_type == 'postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_port=db_port,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_pass=db_pass)
    return connection


def get_tables(path):
    print('path: ', path)
    tables = pd.read_csv(path, sep=':')

    return tables.query('to_be_loaded == "yes"')


