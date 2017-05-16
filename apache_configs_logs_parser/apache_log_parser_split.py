#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ПОРЯДОК ИСПОЛЬЗОВАНИЯ: apache_log_parser_split.py some_log_file

Анализирует содержимое лог-файла и генерирует отчет, содержащий
перечень удаленных хостов, кол-во переданных байт и код состояния
"""

import sys


def dictify_logline(line):
    """
    Parse logline and get: hosts, bytes, status code
    :param line:
    :return: hosts, bytes, status code
    """
    splite_line = line.split()
    return {'remote_host': splite_line[0],
            'status_code': splite_line[8],
            'bytes_sent': splite_line[9]}


def generate_log_report(logfile):
    """
    Read lines and gets bytes sent for each remote hosts
    :param logfile:
    :return: dict {'remote_host':[bytes_sent, ...]}
    """

    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print(line_dict)
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            continue
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)

    return report_dict


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print(__doc__)
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print("You must specity a valid file to parse")
        print(__doc__)
        sys.exit(1)
    log_report = generate_log_report(infile)
    print(log_report)
    infile.close()
