#!/usr/bin/env python
"""
Takes an input data frame and outputs the price per bedroom of
entire apartments (or other unit types, if provided) with a
given minimum score.
"""
import argparse
import os.path
import pandas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputs', nargs='+', type=str)
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-m', '--min', type=float, default=25)
    parser.add_argument('-M', '--max', type=float, default=250)
    args = parser.parse_args()

    if type(args.inputs) == str:
        args.inputs = [args.inputs]

    dataframes = [(infile, pandas.read_csv(infile)) for infile in args.inputs]
    for fname, df in dataframes:
        base = os.path.basename(fname)
        base = os.path.splitext(base)[0]
        cityname = base.split('_')[0]
        plot = seaborn.kdeplot(df['price_per_bedroom'], label=cityname)
        print("median price per bedroom is "
              + str(df['price_per_bedroom'].median())
              + " for " + cityname)

    plt.legend()
    plt.xlabel('Price Per Bedroom')
    plt.ylabel('Distribution Density')
    plot.set(xlim=(args.min, args.max))
    plot.get_figure().savefig(args.output)


if __name__ == "__main__":
    main()
