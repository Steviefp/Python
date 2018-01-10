import time


currentTime = time.strftime("%I:%M:%S")
print(currentTime)
alarmTime=input("What time would you like to wake up at? -> ")


while alarmTime != currentTime:
    currentTime = time.strftime("%I:%M:%S")
    print(currentTime,"This is the current time")
    time.sleep(1)


print("alarm is going off")














'''
import datetime


print("testing")
currentTime=datetime.datetime.now().time()
print(currentTime)
'''