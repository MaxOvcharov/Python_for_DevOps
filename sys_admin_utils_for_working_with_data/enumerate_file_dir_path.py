#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

PATH = '/tmp'


def enumerate_path(path):
    """
    Returns list fo path to all files in dir
    :param path: path name
    :return: list of path to files
    """
    path_collection = []
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            full_path = os.path.join(dir_path, file_name)
            path_collection.append(full_path)
    return path_collection


def enumerate_files(path):
    """
    Returns list fo file from path
    :param path: path name
    :return: list of files from path
    """
    file_collection = []
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            file_collection.append(file_name)
    return file_collection


def enumerate_dirs(path):
    """
    Returns list of subdir from path
    :param path: path name
    :return: list of subdir from path
    """
    subdir_collection = []
    for dir_path, dir_names, file_names in os.walk(path):
        for dir_name in dir_names:
            subdir_collection.append(dir_name)
    return subdir_collection

if __name__ == '__main__':
    print '\nRecursive listing of all paths in a dir\n'
    for path in enumerate_path(PATH):
        print "***  %s  ***" % path

    print '\nRecursive listing of all files in a dir\n'
    for file_name in enumerate_files(PATH):
        print "***  %s  ***" % file_name

    print '\nRecursive listing of all dirs in a dir\n'
    for dir_name in enumerate_dirs(PATH):
        print "***  %s  ***" % dir_name
