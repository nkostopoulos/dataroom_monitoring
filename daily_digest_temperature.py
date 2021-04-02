#!/usr/bin/python

import smtplib
import Adafruit_DHT
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP('SMTPSERVER:25')
s.ehlo("netmode.ntua.gr")

daily_export = open("daily_export_temperature.txt", "r")
html = "<html><body>"
for item in daily_export:
    item = item.rstrip()
    mylist = item.split("&")
    date = mylist[0]
    temp = mylist[1]
    html = html + "<p>" + str(date) + " : " + str(temp) + "</p>"
html = html + "</body></html>"

message = MIMEMultipart("alternative")
message["Subject"] = "Data Room Daily Digest: Temperature"
message["From"] = "FROMMAIL"
message["To"] = "TOMAIL"
text = "Data Room Daily Digest: Temperature"
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
s.sendmail("FROMMAIL","TOMAIL", message.as_string())
