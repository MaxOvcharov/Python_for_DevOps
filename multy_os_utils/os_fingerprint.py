#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script which can research this OS:
Mac OS X
Ubuntu
Red Hat / Cent OS
FreeBSD
SunOS
"""
import platform


class OpSysType(object):
    """Get OS type with the help of platform lib"""
    def __getattr__(self, attr):
        if attr == 'osx':
            return 'Mac OS X'

        elif attr == 'rhel':
            return 'Red Hat'

        elif attr == 'ubu':
            return 'Ubuntu'

        elif attr == 'fbsd':
            return 'FreeBSD'

        elif attr == 'sun':
            return 'SunOS'

        elif attr == 'unknown linux':
            return 'Unknown Linux'

        elif attr == 'unknown':
            return 'Unknown OS'

        else:
            raise AttributeError(attr)

    def linuxType(self):
        """Get Linux type by different params"""
        if platform.dist()[0] == self.rhel:
            return self.rhel
        elif platform.uname()[1] == self.ubu:
            return self.ubu
        else:
            return self.unknown_linux

    def queryOS(self):
        if platform.system() == 'Darwin':
            return self.osx
        elif platform.system() == 'Linux':
            return self.linuxType()
        elif platform.system() == self.sun:
            return self.sun
        elif platform.system() == self.fbsd:
            return self.fbsd


def os_fingerprint():
    os_type = OpSysType()
    print (os_type.queryOS())


if __name__ == '__main__':
    os_fingerprint()
