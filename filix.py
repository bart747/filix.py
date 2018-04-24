#!/usr/bin/env python3.6

import argparse
import os
import re


def collect(new_elm, coll):
    if new_elm not in coll:
        coll.append(new_elm)


def select_by_tags(tags, coll):
    """select entries with given tagnames in titles"""
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                for tag in tags:
                    match = re.search(tag, entry.name, re.I)
                    if match:
                        collect(entry.name, coll)


def print_articles(coll):
    print('files: ', coll)
    for article in coll:
        with open(article, 'r') as f:
            content = f.read()
            print('\n––– ' + article + ': –––\n')
            print(content + '\n')


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(
        description="Find files by using tagnames.\
                     Each tagname should be a string of letters\
                     that's potentialy included in names of files\
                     you want to read.\
                     Content and names of selected files will be displayed\
                     in your terminal.")

    arg_parser.add_argument('tagnames', type=str, nargs="+",
                            help="Tagname (one or many) is a string of letters\
                                  that potentialy exists as a part of a file name(s).")

    args = arg_parser.parse_args()
    collection = []
    select_by_tags(args.tagnames, collection)
    print_articles(collection)
