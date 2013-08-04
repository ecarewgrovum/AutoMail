#!/usr/bin/python

import smtplib

sender = 'bi.h.frank@gmail.com'
receivers = ['bi.h.frank@gmail.com']

message = """From: From Person <frank@frankbi.com>
To: To Person <bi.h.frank@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('localhost', 25)
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
