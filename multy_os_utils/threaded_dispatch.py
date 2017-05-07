#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Multi threading control system with ssh"""

import subprocess
import time

from configparser import ConfigParser
from Queue import Queue
from threading import Thread

start = time.time()
queue = Queue()


def readConfig(conf_file='config.ini'):
    """Gets IPs and commands from config file"""
    config = ConfigParser()
    config.read(conf_file)
    machines = config.items('MACHINES')
    commands = config.items('COMMANDS')
    ips = [ip[1] for ip in machines]
    cmds = [cmd[1] for cmd in commands]
    return ips, cmds


def launcher(i, q, cmd):
    """Run command for ip on separate thread"""
    while True:
        # Get ip and cmd from queue
        ip = q.get()
        print('Thread %s: Running %s to %s' % (i, cmd, ip))
        subprocess.call('ssh root@%s %s' % (ip, cmd), shell=True)
        q.task_done()

# Get IPs and commands from config file
ips, cmds = readConfig()

# Set number of threads
if len(ips) < 25:
    num_threads = len(ips)
else:
    num_threads = 25

# Run threads
for i in range(num_threads):
    for cmd in cmds:
        worker = Thread(target=launcher, args=(i, queue, cmd))
        worker.setDaemon(True)
        worker.start()

print("Main Thread Waiting")
for ip in ips:
    queue.put(ip)

queue.join()
end = time.time()
print('Dispatch Completed in %s seconds' % (end - start))
