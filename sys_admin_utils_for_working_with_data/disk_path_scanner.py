#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Simple model for path recursive walk.
    Run script: dick_path_scanner PATH
    PATH - can be absolute or relative
"""

import os


class RecursivePathWalker(object):
    """ Interface for recursive path walk"""

    def __init__(self, path):
        self.path = path

    def enumerate_path(self):
        """
        Returns generator of path to all files in dir
        :return: generator of path to files
        """
        return (os.path.join(dir_path, file_name)
                for dir_path, dir_names, file_names in os.walk(self.path)
                for file_name in file_names)

    def enumerate_files(self):
        """
        Returns generator of file for the path
        :return: generator of files from path
        """
        return (file_name
                for dir_path, dir_names, file_names in os.walk(self.path)
                for file_name in file_names)

    def enumerate_dirs(self):
        """
        Returns generator of subdir for the path
        :return: generator of subdir
        """
        return (dir_name
                for dir_path, dir_names, file_names in os.walk(self.path)
                for dir_name in dir_names)


if __name__ == '__main__':

    import sys

    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        sys.exit(1)

    if not len(sys.argv) == 2:
        print('PATH is mandatory')
        print(__doc__)
        sys.exit(1)

    PATH = sys.argv[1]
    path_walker = RecursivePathWalker(PATH)
    print('\n--**-- START --**--\n')
    print('1) Recursive listing of all paths in a dir\n')
    for path in path_walker.enumerate_path():
        print(path)

    print('\n2) Recursive listing of all files in a dir\n')
    for file_name in path_walker.enumerate_files():
        print(file_name)

    print('\n3) Recursive listing of all dirs in a dir\n')
    for dir_name in path_walker.enumerate_dirs():
        print(dir_name)
    print('\n--**-- THE END --**--\n')
