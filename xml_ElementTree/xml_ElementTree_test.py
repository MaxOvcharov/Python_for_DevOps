# -*- coding: utf-8 -*-

from xml.etree import ElementTree as ET

tcusers = ET.parse('tomcat-users.xml')
print(tcusers)

first_user = tcusers.find('./user')
print(first_user)

print(first_user.attrib)
print(first_user.get('name'))
print(first_user.tag)
print(first_user.text)

for user in [e for e in tcusers.findall('./user') if e.get('name') == 'tomcat']:
    print(user.attrib)


