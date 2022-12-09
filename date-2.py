import datetime

x = datetime.datetime.now()

print(x.year)

print(x.month)

print(x.day)

print(x.hour)

print(x.minute)

print(x.second)

print(x.microsecond)

print(x.strftime("%A"))#sunday

y = datetime.datetime(2019, 6, 10)

print(y)

print(x.strftime("%B")) #month name in full

print(x.strftime("%a")) #Weekday in short form

print(x.strftime("%w")) #week day as in number

print(x.strftime("%m"))  #month as a number

print(x.strftime("%y")) #year in short form

print(x.strftime("%p")) #returns AM/PM

print(x.strftime("%z")) #timezone

print(x.strftime("%X")) #loca time

print(x.strftime("%c")) #Local version of date and time