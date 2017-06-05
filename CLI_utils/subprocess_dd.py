#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import sys

from subprocess import Popen, PIPE


class ImageFile():
    """Create image of file with the help of dd command"""
    def __init__(self, num=None, size=None, dest=None):
        self.num = num
        self.size = size
        self.dest = dest

    def create_image(self):
        """Create n copy of file images with the size 10Mb"""
        value = '%sMB' % str(self.size/1024)
        for i in range(self.num):
            try:
                cmd = 'dd if=/dev/zero of=%s/file.%s bs=1024 count=%s' \
                      % (self.dest, i, self.size)
                Popen(cmd, shell=True, stdout=PIPE)
            except Exception as e:
                sys.stderr.write(e)

    def controller(self):
        """Runs many of dd command"""
        p = optparse.OptionParser(
            description='Launches many dd command',
            prog='subprocess_dd',
            version='0.1a',
            usage='%prog [options] dest'
        )
        p.add_option('-n', '--number', help='set many dd', type=int)
        p.add_option('-s', '--size', help='size of image in bytes', type=int)
        p.set_defaults(number=10, size=10240)
        options, arguments = p.parse_args()
        if len(arguments) == 1:
            self.dest = arguments[0]
            self.size = options.size
            self.num = options.number
            # run dd commands
            self.create_image()


def main():
    start = ImageFile()
    start.controller()

if __name__ == '__main__':
    main()
