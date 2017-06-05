#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
from configparser import ConfigParser


def read_config(file='hello_config.ini'):
    config = ConfigParser()
    config.read(file)
    sections = config.sections()
    for section in sections:
        phrase = config.items(section)[0][1]
        return phrase


def main():
    p = optparse.OptionParser()
    p.add_option('--sysadmin', '-s')
    p.add_option('--config', '-c', action='store_true')
    p.set_defaults(sysadmin='BOFH')

    options, arguments = p.parse_args()
    if options.config:
        options.sysadmin = read_config()
    print('Hello, %s' % options.sysadmin)

if __name__ == '__main__':
    main()