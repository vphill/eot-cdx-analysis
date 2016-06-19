#!/usr/bin/env python

"""
count08 count12 surt
0   31  100,99,67,134
0   13  118,72,133,174
31  37  2,94,223,66
0   3   218,120,100,94
0   3   249,58,254,173
2   0   58,78,12,76
0   2   67,254,207,130:7123
0   38  af,afghanistan,cdn
50  62  am,circle
"""

import argparse
import csv
import json


def feed_tree(tree, doms, count):
    if len(doms) == 1:
        try:
            tree[doms[0]] = count
        except TypeError:
            tree = {doms[0]: count}
        return tree
    else:
        try:
            subtree = tree[doms[0]]
        except:
            subtree = {}
        try:
            tree[doms[0]] = feed_tree(subtree, doms[1:], count)
        except TypeError:
            tree = feed_tree(subtree, doms[1:], count)
    return tree


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', dest='domain',
                        help='limit to top-level domain')
    parser.add_argument('-m', '--minimum', dest='minimum',
                        type=int, help='minimum number of pages')
    parser.add_argument('-y', '--year', dest='year', default=2008,
                        type=int, help='choose from 2008 or 2012')
    args = parser.parse_args()

    tree = {}
    # with open('test.csv') as csvfile:
    with open('../data/surt-count-combined.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            # eliminate bare ip addresses
            try:
                if not row['surt'][0].isalpha():
                    continue
            except Exception as e:
                continue
            # limit domain if requested
            if args.domain:
                if not row['surt'].startswith('%s,' % args.domain):
                    continue
            # choose from one year or the other
            if args.year == 2012:
                count = int(row['count12'])
            else:
                count = int(row['count08'])
            doms = row['surt'].split(':')[0].split(',')
            if args.minimum and count < args.minimum:
                continue
            tree = feed_tree(tree, doms[:], count)

    print(json.dumps(tree, indent=2))
