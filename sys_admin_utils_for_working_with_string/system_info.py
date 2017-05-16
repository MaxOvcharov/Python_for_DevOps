#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:" % uname
subprocess.call([uname, uname_arg])

diskspace = "df"
diskspace_arg = "-h"
print "\nGathering diskspace information with %s command:" % diskspace
subprocess.call([diskspace, diskspace_arg])