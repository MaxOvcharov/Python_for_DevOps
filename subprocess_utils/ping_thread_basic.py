#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script runs two groups of threads and uses two queues.
First group of threads ping ips from first queue.
Second groups of threads get MAC from second queue for alive ips.
"""
import re
import subprocess

from threading import Thread
from queue import Queue

num_ping_threads = 3
num_arp_threads = 3
in_queue = Queue()
out_queue = Queue()

ips = ['10.0.1.1', '10.0.1.3', '10.0.1.11', '10.0.1.51']


def pinger(i, iq, oq):
    """ Ping subnet """
    while True:
        ip = iq.get()
        print('Thread %s: Pinging %s' % (i, ip))
        ret = subprocess.call('ping -c 1 %s' % ip,
                              shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)
        if ret == 0:
            # Add ip to the second queue
            oq.put(ip)
        else:
            print('% did not respond' % ip)
        iq.task_done()


def arping(i, oq):
    """Get MAC for ips from second queue"""
    while True:
        ip = oq.get()
        p = subprocess.Popen('arping - 1 %s' % ip,
                            shell=True,
                            stdout=subprocess.PIPE)
        out = p.stdout.read()
        result = out.split()
        pattern = re.compile(':')
        mac_address = [item for item in result if re.search(pattern, item)]
        print('IP Address: %s | MAC Address: %s' % (ip, mac_address[0]))
        oq.task_done()

# Put ips into first queue

for ip in ips:
    in_queue.put(ip)

# Run first group of threads for ping method
for i in range(num_ping_threads):
    worker = Thread(target=pinger, args=(i, in_queue, out_queue))
    worker.setDaemon(True)
    worker.start()

# Run second group of threads for arping method
for i in range(num_arp_threads):
    worker = Thread(target=arping, args=(i, out_queue))
    worker.setDaemon(True)
    worker.start()

print('Main Thread Waiting')
in_queue.join()
out_queue.join()
print('Done all tasks')
