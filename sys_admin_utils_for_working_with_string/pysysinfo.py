#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

from sys_admin_utils_for_working_with_string.system_info_func import diskspace_func


def dir_space(path):
    dir_usage = "du"
    dir_arg = "-h"
    print('Space used in %s dirctory' % path)
    subprocess.call([dir_usage, dir_arg, path])


def main():
    dir_space("/tmp")
    diskspace_func()

if __name__ == "__main__":
    main()
