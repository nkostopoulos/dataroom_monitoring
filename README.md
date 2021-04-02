# dataroom_monitoring
Scripts used in our data room to monitor temperature and humidity (based on Raspberry Pi v3)
  
This repository includes the following scripts:  
test.py: a script to get the current temperature and humidity of the data room.  
alarm.py: a script that triggers an alarm if the temperature exceeds a predefined threshold. At the same time, measurements are collected in .txt files.  
daily_digest_temperature.py: a script that returns the temperature and humidity measurements of the previous day.  
  
Remember to change the variables with capital letters with their appropriate values (FROMSERVER, TOSERVER, SMTPSERVER).  
