# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import mimetypes

from_addr = 'EMAIL_FROM'
to_addr = 'EMAIL_TO'
subject_header = 'Subject: Sending PDF Attachment'
attachment = 'disk_report.pdf'
body = "This message sends a PDF attachment created with ReportLab."

m = MIMEMultipart()
m["To"] = to_addr
m["From"] = from_addr
m["Subject"] = subject_header

ctype, encoding = mimetypes.guess_type(attachment)
print ctype, encoding

maintype, subtype = ctype.split('/', 1)
print maintype, subtype

m.attach(MIMEText(body))
fp = open(attachment, 'rb')
msg = MIMEBase(maintype, subtype)
msg.set_payload(fp.read())
fp.close()

encoders.encode_base64(msg)
msg.add_header('Content-Disposition', 'attachment', file=attachment)
m.attach(msg)

s = smtplib.SMTP_SSL('smtp.DOMAIN.RU')
s.set_debuglevel(1)
s.login('EMAIL', 'PASSWORD')
s.sendmail(from_addr, to_addr, m.as_string())
s.quit()

