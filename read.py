from util import get_connection


def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_connection(db_type=SOURCE_DB['DB_TYPE'],
                                db_host=SOURCE_DB['DB_HOST'],
                                db_port=SOURCE_DB['DB_PORT'],
                                db_name=SOURCE_DB['DB_NAME'],
                                db_user=SOURCE_DB['DB_USER'],
                                db_pass=SOURCE_DB['DB_PASS']
                                )
    cursor = connection.cursor()
    if limit == 0:
        query = 'SELECT * FROM {}'.format(table_name)
    else:
        query = 'SELECT * FROM {} LIMIT {}'.format(table_name, limit)
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names

    connection.close()

    return data, column_names



# from mysql import connector as mc
# from config import DB_DETAILS
#
# def connect_db():
#     db_details = DB_DETAILS['dev']
#     source_db= db_details['SOURCE_DB']
#
#     print(source_db)
#
#     connection = mc.connect(
#         user=source_db['DB_USER'],
#         password=source_db['DB_PASS'],
#         host=source_db['DB_HOST'],
#         port=source_db['PORT'],
#         database=source_db['DB_NAME'])

# connection = mc.connect(user='root',password='admin123',host='localhost',port=3307,database='sourceDB')

