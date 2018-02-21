#!/usr/bin/env python
"""
Takes an input data frame and outputs the price per bedroom of
entire apartments (or other unit types, if provided) with a
given minimum score.
"""
import argparse
import sys
import pandas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'))
    parser.add_argument('-m', '--minscore', type=float, default=4.0)
    parser.add_argument('-u', '--unittype', default="Entire home/apt")
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args()

    data = pandas.read_csv(args.input)
    data = data[data['room_type'] == args.unittype]
    data = data[data['overall_satisfaction'] >= args.minscore]

    price_per_bedroom = data['price']/data['bedrooms']
    df = pandas.DataFrame()
    df['price_per_bedroom'] = price_per_bedroom
    df.to_csv(args.output)


if __name__ == "__main__":
    main()
