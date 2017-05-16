# -*- coding: utf-8 -*-

import poplib

username = 'USER NAME'
password = 'PASSWORD'
port = 995

mail_server = 'pop.DOMAIN.RU'

p = poplib.POP3_SSL(mail_server, port)
try:
    p.user(username)
    p.pass_(password)
except Exception as e:
    print("Error handel: " + str(e))

for msg_id in p.list()[1]:
    # get all emails from email box
    print(msg_id)
    outf = open('%s.eml' % msg_id, 'w')
    outf.write('\n'.join(p.retr(msg_id)[1]))
    outf.close()
p.quit()
