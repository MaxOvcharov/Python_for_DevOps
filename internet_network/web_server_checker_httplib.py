#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
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
    try:
        conn = httplib.HTTPConnection(address, port)
        print 'HTTP connection created successfully'
        # Sent request
        req = conn.request('GET', resource)
        print 'Request for %s successfull' % resource
        # Get response
        response = conn.getresponse()
        print 'Response status %s' % response.status
    except httplib.error, e:
        print 'HTTP connection failed: %s' % e
        return False
    finally:
        print 'HTTP connection closed successfully'
    if response.status in [200, 301]:
        return True
    else:
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
    print 'Options: %s, args: %s' % (options, args)
    check = check_webserver(options.address, options.port, options.resource)
    print 'Check_webserver returned %s' % check
    sys.exit(not check)
