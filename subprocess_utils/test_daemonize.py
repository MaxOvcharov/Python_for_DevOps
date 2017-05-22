#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script tests daemonize script
"""
import sys
import time

from daemonize_process import daemonize


def mod_5_watcher():
    start_time = time.time()
    end_time = start_time + 20
    while time.time() < end_time:
        now = time.time()
        if int(now) % 5:
            sys.stderr.write('Mod 5 at %s sec\n' % now)
        else:
            sys.stdout.write('Mod 5 at %s sec\n' % now)
        time.sleep(1)

if __name__ == '__main__':
    daemonize(stdout='/tmp/stdout.log', stderr='/tmp/stderr.log')
    mod_5_watcher()
