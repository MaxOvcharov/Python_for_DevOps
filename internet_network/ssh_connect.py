#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

hostname = 'IP ADDRESS'
port = 22
username = 'USER NAME'
password = 'USER PASSWORD'

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    # Added host name in to known host if not exist
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname,
              port=port,
              username=username,
              password=password)

    stdin, stdout, stderror = s.exec_command('ls -lah')
    print stdout.read()
    s.close()
