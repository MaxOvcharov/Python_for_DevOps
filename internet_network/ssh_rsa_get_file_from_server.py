#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import os

hostname = 'IP ADDRESS'
port = 22
username = 'USER NAME'
dir_path = '/home/USER_NAME/logs'
pkey_file = '/home/USER_NAME/.ssh/id_rsa'

if __name__ == '__main__':
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files =sftp.listdir(dir_path)
    for file in files:
        print 'Retrieving: %s' % file
        sftp.get(os.path.join(dir_path, file), file)
    t.close()
