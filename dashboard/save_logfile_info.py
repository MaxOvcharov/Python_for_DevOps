# -*- coding: utf-8 -*-

import shelve
from apache_configs_logs_parser import  apache_log_parser_regex

logfile = open('access.log', 'r')
shelve_file = shelve.open('access.s')

for line in logfile:
    d_line = apache_log_parser_regex.dictify_logline(line)
    shelve_file[d_line['remote_host']] = \
        shelve_file.setdefault(d_line['remote_host'], 0) + int(d_line['byte_sent'])

logfile.close()
shelve_file.close()
