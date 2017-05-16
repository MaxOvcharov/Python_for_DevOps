#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from checksum_checker import create_checksum
from disk_path_scanner import RecursivePathWalker
from os.path import getsize


def find_duplicates(path='/tmp'):
    """
    Recursive finder of all duplicate path
    :param path: paht name
    :return:
    """
    dup = []
    record = {}
    d = RecursivePathWalker(path)
    files = d.enumerate_path()
    for file in files:
        compound_key = (getsize(file), create_checksum(file))
        if compound_key in record:
            dup.append(file)
        else:
            record[compound_key] = file
    return dup

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Find duplicates for default dir -> /tmp')
        duplicates = find_duplicates()
    else:
        duplicates = find_duplicates(sys.argv[1])
    print('//-//-' * 9 + '\n')
    for dup in enumerate(duplicates, start=1):
        print('%s) Duplicate file: %s" % dup')
