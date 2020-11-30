import datetime
from datetime import date

mytime = datetime.time(2, 20)

print(mytime)

print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)


print(type(mytime))

today = datetime.date.today()
print(today)

print(today.day)
print(today.month)
print(today.year)

print(today.ctime())

mydate_time = datetime.datetime(2021, 10, 3, 14, 20, 1)
print(mydate_time)

mydate_time = mydate_time.replace(year=2020)
print(mydate_time)

#Arithmetic

#Date

date1 = date(2021, 11, 3)
date2 = datetime.date.today()

results = date1 - date2
print(results)

#Datetime

datetime_one = datetime.datetime(2021, 11, 3, 22, 0)
datetime_two = datetime.datetime(2020, 11, 3, 12, 0)

result = datetime_one - datetime_two
print(result)
print(result.seconds)