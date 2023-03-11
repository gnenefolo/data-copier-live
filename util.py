import pandas as pd


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_load == "yes"')


if __name__ == '__main__':
    pass
