#example-1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ElIf
#example
a1 = 33
b1 = 33
if b1 > a1:
  print("b is greater than a")
elif a1 == b1:
  print("a and b are equal")

#Else
#example

a2 = 200
b2 = 33
if b2 > a2:
  print("b is greater than a")
elif a2 == b2:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short Hand If ... Else
#example-1
a3=375
b3=33
if a3 > b3: print("a is greater than b")

#example-2
a4 = 33
b4 = 375
print("A") if a4 > b4 else print("B")

#And \ Or \ Nested if 
#example
name = "Anderson"
number = int(input())
if name == "Anderson":
    if number == 375 and int((number%100)/10) == 7:
        print("YES")
    elif number == 355 or (number%100)/10 == 5:
        print("Yes")
    else:
        print("NO")
