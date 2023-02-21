import datetime
x1 = datetime.datetime.now()
print(x1)

print()
#example 1
x2 = datetime.datetime(x1.year, x1.month, x1.day - 5, x1.hour, x1.minute, x1.second , x1.microsecond)
print(x2)

print()
#example 2
for i in range(-1,2):
    print(x1.day + i)

print()
#example 3
x3 = datetime.datetime(x1.year, x1.month, x1.day, x1.hour, x1.minute, x1.second)
print(x3)

print()
#example 4
bday = datetime.datetime(2004, 7, 7, 14, 12, 50)
x4 = x1-bday
print(x4)
