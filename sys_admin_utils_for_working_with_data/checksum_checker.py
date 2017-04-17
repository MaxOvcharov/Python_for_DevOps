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
    with open(path) as f:
        checksum = hashlib.md5
        while True:
            buffer = f.read(8192)
            if not buffer:
                break
            checksum.update(buffer)
    checksum = checksum.digest()
    return checksum
