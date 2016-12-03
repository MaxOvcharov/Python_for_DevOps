#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess


def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:" % uname
    subprocess.call([uname, uname_arg])


def diskspace_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print "\nGathering diskspace information with %s command:" % diskspace
    subprocess.call([diskspace, diskspace_arg])


def main():
    uname_func()
    diskspace_func()

main()
