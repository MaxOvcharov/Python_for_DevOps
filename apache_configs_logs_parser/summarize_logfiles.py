#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create report for Apache logfiles. You can use
--consolidate or --regex keys for creating report
"""
from optparse import OptionParser


def open_files(files):
    for f in files:
        yield (f, open(f))


def combine_lines(files):
    for f, f_obj in files:
        for line in f_obj:
            yield line


def obfuscate_ipaddr(addr):
    return '.'.join(str((int(n)/10) * 10) for n in addr.split('.'))

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c', '--consolidate', dest='consolidate',
                      default=False, action='store_true',
                      help='consolidate log files')
    parser.add_option('-r', '--regex', dest='regex', default=False,
                      action='store_true', help='use regex parser')
    options, args = parser.parse_args()
    logfiles = args
    if options.regex:
        from apache_log_parser_regex import generate_log_report
    else:
        from apache_log_parser_split import generate_log_report
    opend_files = open_files(logfiles)

    if options.consolidate:
        opend_files = (('CONSOLIDATED', combine_lines(opend_files)),)
    for filename, file_obj in opend_files:
        print('*' * 60)
        print(filename)
        print('-' * 60)
        print('%-20s%s' % ('IP ADDRESS', 'BYTES TRANSFERRED'))
        print('-' * 60)
        report_dict = generate_log_report(file_obj)
        for ip_addr, bytes in report_dict:
            print('%-20s%s' % (obfuscate_ipaddr(ip_addr), sum(bytes)))
        print('=' * 60)