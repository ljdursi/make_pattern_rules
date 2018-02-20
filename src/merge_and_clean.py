#!/usr/bin/env python3
import argparse
import sys
import os
import pandas


def merge_dataframes(input_dir):
    """
    Reads in all CSV files in the provided directory, and converts
    'last_modified' column to a datetime, and extracts year
    Also removes unused columns, and removes some spurious entries
    (zero reviews, or zero bedrooms)

    :param input_dir: Input directory to search for CSVs
    :returns: concatenated dataframe of all CSVs
    """
    files = os.listdir(input_dir)
    dfs = [pandas.read_csv(os.path.join(input_dir, f))
           for f in files if f.endswith(".csv")]
    df_all = pandas.concat(dfs)

    df_all.drop('country', axis=1, inplace=True)
    df_all.drop('borough', axis=1, inplace=True)
    df_all.drop('bathrooms', axis=1, inplace=True)
    df_all.drop('location', axis=1, inplace=True)

    df_all = df_all[df_all['bedrooms'] > 0]
    df_all = df_all[df_all['reviews'] > 0]

    df_all.last_modified = pandas.to_datetime(df_all.last_modified)
    df_all['lm_year'] = pandas.DatetimeIndex(df_all.last_modified).year
    return df_all


def year_filter(all_data, year=None):
    """
    Returns the data frame filtered by year if year is specified
    """
    if year is not None:
        return all_data[all_data['lm_year'] == year]
    return all_data


def last_row_per_room_id(all_data):
    """
    To avoid double-counting (since each row itself is an aggregate),
    only choose the last row per roomID
    """
    grpd = all_data.groupby(['room_id'])
    latest = all_data.iloc[grpd.apply(lambda x: x['last_modified'].idxmax())]
    return latest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str)
    parser.add_argument('-y', '--year', type=int)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args()

    data = merge_dataframes(args.dir)
    filtered_data = year_filter(data, args.year)
    merged_data = last_row_per_room_id(filtered_data)

    merged_data.to_csv(args.output)


if __name__ == "__main__":
    main()
