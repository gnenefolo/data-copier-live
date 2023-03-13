import sys
from config import DB_DETAILS
from util import get_tables
from read import read_table
from write import load_table


def main():
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list')
    for table_name in tables['table_name']:
        print(f'Reading data for {table_name}')
        data, column_name = read_table(db_details, table_name)
        print(f'Loading data in {table_name}')
        load_table(db_details, data, column_name, table_name)


if __name__ == '__main__':
    main()
