#! /usr/bin/env python
""" pandas-readcsv.py, by Jan Hamara, 2018-01-10

    This script uses Pandas DataFrames to treat data from CSV file
"""

import pandas as pd


def main():
    data = pd.read_csv('data.csv')
    data_rows = data.iloc[0:5]

    print(data_rows[['Username','Password']])

if __name__ == '__main__':
    main()


