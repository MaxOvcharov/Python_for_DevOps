#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def create_checksum(path):
    """
    Read file and chechsum for avery line in file.
    Return full checksum of the file
    :param path: path to the file
    :return: full checksum of the file
    """
    checksum = hashlib.md5()
    try:
        with open(path) as f:
            while True:
                tmp_buffer = f.read(8192)
                if not tmp_buffer:
                    break
                checksum.update(tmp_buffer)
        checksum = checksum.digest()
    except IOError, e:
        print "Unsupported file format: %s" % e
    return checksum
