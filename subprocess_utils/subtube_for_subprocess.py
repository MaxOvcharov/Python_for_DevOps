#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script runs consistently some subprocess call
"""

import subprocess
import time


class BaseArgs(object):
    """ Abstract class which split named params """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        if self.kwargs.get('delay'):
            self.delay = self.kwargs['delay']
        else:
            self.delay = 0
        if self.kwargs.get('verbose'):
            self.verbose = self.kwargs['verbose']
        else:
            self.verbose = False

    def run(self):
        raise NotImplementedError


class Runner(BaseArgs):
    """
    This class runs consistently subprocess.call() for some commands from
    From named params.
    Example:
        cmd = Runner('ls -lah', 'df -h', verbose=True, delay=3)
        cmd.run()
    """
    def run(self):
        for cmd in self.args:
            if self.verbose:
                print("\nRunning %s with delay=%s sec:" % (cmd, self.delay))
            time.sleep(self.delay)
            subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    cmd = Runner('ls -lah', 'df -h', verbose=True, delay=3)
    cmd.run()
