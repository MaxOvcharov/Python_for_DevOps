# -*- coding: utf-8 -*-

import smtplib
mail_server = "smtp.rambler.ru"
mail_server_port = 465
from_addr = 'EMAIL_FROM'
to_addr = 'EMAIL_TO'

from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s\r\n\r\n' % to_addr
subject_header = 'Subject: Testing SMTP Authentication'

body = 'This mail tests SMTP Authentication'

email_message = '%s\n%s\n%s\n\n%s' % (from_header, to_header, subject_header, body)

s = smtplib.SMTP_SSL(mail_server, mail_server_port)
s.set_debuglevel(1)
s.login('EMAIL', 'PASSWORD')
s.sendmail(from_addr, to_addr, email_message)
s.quit()


