#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script daemonize runinng process
"""
import os
import sys


def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    #  Run first fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # First parent process closed
    except OSError as e:
        sys.stderr.write('Fork #1 failed: (%d) %s\n' % (e.errno, e.strerror))
        sys.exit(1)
    #  Unset from parent process
    os.chdir('/')
    os.umask(0)
    os.setsid()
    #  Run second fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # Second parent process closed
    except OSError as e:
        sys.stderr.write('Fork #2 failed: (%d) %s\n' % (e.errno, e.strerror))
        sys.exit(1)
    # Now process is daemonized
    for f in sys.stdout, sys.stderr:
        f.flush()
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
