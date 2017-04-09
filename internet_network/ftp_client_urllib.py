#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RUN SCRIPT: ftp_client_urllib.py URL FILENAME
PARAMS:
    URL - it's address to FTP server
        1) ftp://[username[:password]@]hostname/filename
        2) ftp://username:password@hostname/%2Fpath/to/myfile.txt - if you want to download file by absolute path

    FILENAME - absolute path or path to file
"""

import urllib
import sys

if '-h' in sys.argv or '--help' in sys.argv:
    print __doc__
    sys.exit(1)

if not len(sys.argv) == 3:
    print 'URL and FILENAME are mandatory'
    print __doc__
    sys.exit(1)

url = sys.argv[1]
file_name = sys.argv[2]
try:
    urllib.urlretrieve(url, file_name)
except Exception, e:
    print "CRITICAL ERROR; %s" % e
