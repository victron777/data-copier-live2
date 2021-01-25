from util import get_connection


def build_insert_query(table_name, column_names):
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names ))
    column_values_string = ', '.join(column_values)

    query = ('''
        INSERT INTO {} ({}) VALUES ({})
    '''.format(table_name, column_names_string, column_values_string))
    return query


def insert_data(connection, cursor, query, data, batch_size=100):
    recs = []
    count = 1
    for rec in data:
        recs.append(rec)
        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            recs = []

        count += 1

    cursor.executemany(query, recs)
    connection.commit()
    connection.close()


def load_table(db_details, data, column_names, table_name):
    TARGET_DB = db_details['TARGET_DB']
    # print(TARGET_DB)
    connection = get_connection(db_type=TARGET_DB['DB_TYPE'],
                                db_host=TARGET_DB['DB_HOST'],
                                db_port=TARGET_DB['DB_PORT'],
                                db_name=TARGET_DB['DB_NAME'],
                                db_user=TARGET_DB['DB_USER'],
                                db_pass=TARGET_DB['DB_PASS']
                                )
    # print("Type(connection): ", type(connection))
    cursor = connection.cursor()
    query = build_insert_query(table_name, column_names)
    insert_data(connection, cursor, query, data)

    connection.close()












# import psycopg2
#
# connection = psycopg2.connect("dbname=postgres user=postgres host=0.0.0.0 password=admin123 port=5432")
# cursor = connection.cursor()
# query = "INSERT INTO departments (department_id, department_name) VALUES (1,'testing1')"
# cursor.execute(query)
# connection.commit()
# connection.close()
