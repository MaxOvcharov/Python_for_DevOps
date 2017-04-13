#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

hostname = 'IP ADDRESS'
port = 22
username = 'USER NAME'
password = 'USER PASSWORD'

if __name__ == '__main__':
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname,
              port=port,
              username=username,
              password=password)

    channel = s.get_transport().open_session()
    channel.get_pty()
    channel.settimeout(5)
    channel.exec_command('sudo ls')
    channel.send(password + '\n')
    print channel.recv(1024)

    channel.close()
    s.close()
