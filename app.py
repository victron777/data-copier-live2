import sys
from util import get_tables, load_db_details
from read import read_table
from write import load_table


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('/home/victor/IdeaProjects/data-copier-live/table_list')

    for table_name in tables['table_name']:
        print('Reading data for {}'.format(table_name))
        data, column_names = read_table(db_details, table_name)
        # print(column_names)
        print('Loading data for {}'.format(table_name))
        load_table(db_details, data, column_names, table_name)


if __name__ == '__main__':
    main()
