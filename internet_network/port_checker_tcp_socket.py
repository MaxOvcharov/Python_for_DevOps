#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys


def check_server(address, port):
    """Create socket package"""
    s = socket.socket()
    print "Attempting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        print "Connected to %s on port %s" % (address, port)
        return True
    except socket.error, e:
        print "Connection to %s on port %s failed" % (address, port)
        return False

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a', '--address', dest='address', default='localhost',
                      help='ADDRESS for server', metavar='ADDRESS')
    parser.add_option('-p', '--port', dest='port', type='int', default=80,
                      help='PORT for server', metavar='PORT')
    (options, args) = parser.parse_args()
    print 'Options: %s, args: %s' % (options, args)
    check = check_server(options.address, options.port)
    print 'Check_server returned %s' % check
    sys.exit(check)
