#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()

print "\n{}\n".format(uname)

print "Checking IN and NOT IN: "
if 'Linux' in uname:
    print '1)\tLinux IN uname'

if 'Darwing' not in uname:
    print '2)\tDarwing NOT IN name\n'

print "Checking find() and index() functions: "

print '1) Index of starting substring "Linux" is -\t{0}'.format(uname.index('Linux'))
print '2) Find of starting substring "Linux" is -\t{0}'.format(uname.find('Linux'))

try:
    print '3) Index of starting substring "Darwing" is -\t{0}'.format(uname.index('Darwing'))
except ValueError, e:
    print '3) Index of starting substring "Darwing" is -\tValueError: {0}'.format(str(e).strip())

print '4) Find of starting substring "Darwing" is -\t{0}\n'.format(uname.find('Darwing'))

print "Checking slice of string: "

smp_index = uname.index('SMP')
print '1) Print from start of the substring to the end of the string:\t{}'.format(uname[smp_index:])
print '2) Print from start of the string to the start of the substring:\t{}'.format(uname[:smp_index])
