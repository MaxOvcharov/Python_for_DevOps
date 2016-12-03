#!/usr/bin/env python
# -*- coding: utf-8 -*-
from system_info_func import diskspace_func
import subprocess


def dir_space(path):
    dir_usage = "du"
    dir_arg = "-h"
    print "Space used in %s dirctory" % path
    subprocess.call([dir_usage, dir_arg, path])


def main():
    dir_space("/tmp")
    diskspace_func()

if __name__ == "__main__":
    main()
