#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import socket
import sys


def check_webserver(address, port, resource):
    """ Check web-server by tcp
        :param address: domain
        :param port: web-server port number
        :param resource: http headers
        :return: True - success connection or False - fail connection
    """
    # Create http resource line
    if not resource.startswith('/'):
        resource = '/' + resource
    request_string = 'GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (resource, address)
    print('HTTP request:')
    print('|||%s|||' % request_string)

    # Create socket connection
    s = socket.socket()
    print('Attempting to connect to %s on port %s' % (address, port))
    try:
        s.connect((address, port))
        print('Connected to %s on port %s' % (address, port))
        s.send(request_string)
        # Get first 100 bytes
        rsp = s.recv(100)
        print('Received 100 bytes of HTTP responce')
        print('|||%s|||' % rsp)
    except socket.error as e:
        print('Connection to %s on port %s failed: %s' % (address, port, e))
        return False
    finally:
        # Close socket connection
        print('Closing the connection...')
        s.close()

    lines = rsp.splitlines()
    print('First line of HTTP responce: %s' % lines[0])
    try:
        version, status, message = re.split(r'\s+', lines[0], 2)
        print('Version: %s, status: %s, massage: %s' % (version, status, message))
    except ValueError:
        print('Failed to splite status line')
        return False
    if status in ['200', '301']:
        print('Success - status was %s' % status)
        return True
    else:
        print('Status was %s' % status)
        return False

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('-a', '--address', dest='address', default='localhost',
                      help='ADDRESS for webserver', metavar='ADDRESS')
    parser.add_option('-p', '--port', dest='port', type='int', default=80,
                      help='PORT for webserver', metavar='PORT')
    parser.add_option('-r', '--resource', dest='resource', default='index.html',
                      help='RESOURCE to check', metavar='RESOURCE')
    (options, args) = parser.parse_args()
    print('Options: %s, args: %s' % (options, args))
    check = check_webserver(options.address, options.port, options.resource)
    print('Check_webserver returned %s' % check)
    sys.exit(not check)
