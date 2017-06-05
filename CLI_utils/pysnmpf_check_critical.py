#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import re

from subprocess import Popen, PIPE


def main():
    p = optparse.OptionParser(
        description='Python wrapped snmpdf command',
        prog='pysnmpdf',
        version='0.1a',
        usage='%prog machine'
    )
    p.add_option('-c', '--community', help='snmp community string')
    p.add_option('-V', '--Version', help='snmp version to use')
    p.set_defaults(community='public', Version='2c')
    options, arguments = p.parse_args()
    SNMPDF = 'snmpdf'
    if len(arguments) == 1:
        machine = arguments[0]

        def parse():
            """Return generator with the string from snmpdf command"""
            ps = Popen([SNMPDF, '-c', options.community, '-v', options.Version, machine],
                       stdout=PIPE, stderr=PIPE)
            return ps.stdout

        # Find CRITICAL value in the string from command
        pattern = '9[0-9]%'
        outline = (line.split() for line in parse())
        flag = (''.join(row) for row in outline if re.search(pattern, row[-1]))
        for line in flag:
            print('%s CRITICAL' % line)
        # Example: Real Memory 234324 2343242 2343242 95% CRITICAL
    else:
        p.print_help()

if __name__ == '__main__':
    main()