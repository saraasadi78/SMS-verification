import datetime
import time
import subprocess
from textwrap import dedent
import requests
from threading import Timer
import calendar
from kavenegar import *


api = KavenegarAPI('49396E332B65484C53354947654B6854467A595063462F42426D352B766365495569616D35452F464B2F453D' , timeout=20)

x=datetime.today()
y=x.replace(day=x.day+1,hour=2,minute=30,second=0,microsecond=0)
delta_t=y-x
secs=delta_t.seconds+1

def my_message():
    print("hi this message will display in 2:30 AM ")
    
t=Timer(secs,my_message)
t.start()


now=datetime.datetime.now()

today_time=datetime.date.today()

current_year=now.year

current_month=now.month

last_day_of_month=calendar.monthrange(current_year, current_month)[1]

if today_time==last_day_of_month:
    url="https://api.kavenegar.com/v1/49396E332B65484C53354947654B6854467A595063462F42426D352B766365495569616D35452F464B2F453D/sms/sendjason"
    pyload = {'sender': '100047778',
              'receptor': '09145031575',
              'message': 'Hello this is my first sms'}

    response = api.sms_send(pyload)
    print(response)

else:
    print("today is not last day of month")










