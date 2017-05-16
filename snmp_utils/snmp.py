#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netsnmp


class Snmp(object):
    """Simple SNMP connection """

    def __init__(self,
                 oid='sysDescr',
                 version=2,
                 dest_host='localhost',
                 community='public'):

        self.oid = oid
        self.version = version
        self.dest_host = dest_host
        self.community = community

    def query(self):
        """Simple SNMP query"""
        try:
            result = netsnmp.snmwalk(self.oid,
                                     version=self.version,
                                     destHost=self.dest_host,
                                     community=self.community)
        except Exception as e:
            print("HANDLE ERROR: %s" % e)
            result = None
        return result
