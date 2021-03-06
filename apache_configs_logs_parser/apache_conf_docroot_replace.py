#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from io import StringIO

vhost_start = re.compile(r'<VirtualHost\s+(.*?)>')
vhost_end = re.compile(r'</VirtualHost')
docroot_re = re.compile(r'(DocumentRoot\s+)(\S+)')


def replace_docroot(conf_string, vhost, new_docroot):
    """
        Отыскивает в файле httpd.conf строки DocumentRoot,
        соответствующие указанному vhost, и замещает их новыми
        строками new_docroot
    """
    conf_file = StringIO(conf_string)
    in_vhost = False
    curr_vhost = None
    for line in conf_file:
        vhost_start_match = vhost_start.search(line)
        if vhost_start_match:
            curr_vhost = vhost_start_match.groups()[0]
            in_vhost = True
        if in_vhost and (curr_vhost == vhost):
            docroot_match = docroot_re.search(line)
            if docroot_match:
                sub_line = docroot_re.sub(r'\1%s' % new_docroot, line)
                conf_string = conf_string.replace(line, sub_line)
                vhost_end_match = vhost_end.search(sub_line)
                if vhost_end_match:
                    in_vhost = False
                print(sub_line)
    return conf_string

if __name__ == '__main__':
    import sys
    conf_file = sys.argv[1]
    vhost = sys.argv[2]
    docroot = sys.argv[3]
    conf_string = open(conf_file).read()
    with open(conf_file, 'w') as f:
        f.write(replace_docroot(conf_string, vhost, docroot))