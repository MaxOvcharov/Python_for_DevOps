#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Find difference between filenames in two dirs
"""
import os
import sys
import time

from subprocess import call
from threading import Timer


class EventLoopDelaySpawn(object):
    """Event handler which runs thread method with delay"""
    def __init__(self, poll=10, wait=1, verbose=True,
                 dir1='/tmp/dir1', dir2='/tmp/dir2'):
        self.poll = poll
        self.wait = wait
        self.verbose = verbose
        self.dir1 = dir1
        self.dir2 = dir2

    def poller(self):
        """Generate poll interval"""
        time.sleep(self.poll)
        if self.verbose:
            print('Polling at %s sec interval' % self.poll)

    def action(self):
        time.sleep(self.wait)
        if self.verbose:
            print('Wailing %s seconds to run Action' % self.wait)
        ret = call('rsync -av --delete %s/%s' % (self.dir1, self.dir2), shell=True)

    def eventHandler(self):
        if os.listdir(self.dir1) != os.listdir(self.dir2):
            print(os.listdir(self.dir1))
            t = Timer((self.wait), self.action)
            t.start()
            if self.verbose:
                print('Event Registered')
        else:
            if self.verbose:
                print('No Event Registered')

    def run(self):
        """Run event loop with delay"""
        try:
            while True:
                self.eventHandler()
                self.poller()
        except Exception as e:
            print('Error: %s' % e)
        finally:
            sys.exit(0)

if __name__ == '__main__':
    E = EventLoopDelaySpawn()
    E.run()
