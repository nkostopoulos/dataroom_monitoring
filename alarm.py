#!/usr/bin/python

import smtplib
import Adafruit_DHT
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import subprocess

def save_output(command):
    proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    (out,err)=proc.communicate()
    outwithoutreturn=out.rstrip('\n')
    return outwithoutreturn

s = smtplib.SMTP('SMTPSERVER:25')
s.ehlo("netmode.ntua.gr")

humidity, temperature = Adafruit_DHT.read_retry(11,17)

if temperature is None or humidity is None:
    sys.exit(1)

out = save_output("date")
daily_export_temperature = open("daily_export_temperature.txt", "a")
daily_export_temperature.write(str(out) + " & " + str(temperature) + "\n")
daily_export_humidity = open("daily_export_humidity.txt", "a")
daily_export_humidity.write(str(out) + " & " + str(humidity) + "\n")


if temperature >= 28:
    message = MIMEMultipart("alternative")
    message["Subject"] = "Data Room Alert, Temperature"
    message["From"] = "FROMMAIL"
    message["To"] = "TOMAIL"
    text = "Data Room Alert. Temperature: " + str(temperature)
    html = "<html><body><p>Data Room Alert. Temperature: " + str(temperature) + "</p></body></html>"
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    s.sendmail("FROMMAIL","TOMAIL", message.as_string())
