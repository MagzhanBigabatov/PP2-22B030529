#For loops
#example-1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print()
#example-2
for x1 in "Computer":
    print(x1)

print()
#example-3 break
game = ["CS-GO", "CS-S", "CS 1.6"]
for x2 in game:
    print(x2)
    if x2 == "CS-S":
        break

print()
#example-3 but if print after if
game1 = ["CS-GO", "CS-S", "CS 1.6"]
for x3 in game:
    print(x3)
    if x3 == "CS-S":
        break

print()
#example-4 continue
gameX = ["GTA 5", "DOOM 64", "Dead Space", "Dying Light"]
for x4 in gameX:
    if x4 == "DOOM 64":
        continue
    print(x4)

print()
#example-5 range from 0 to number
for a in range(5):
    print(a)

print()
#example-6 range from number1 to number2
for b in range(3, 7):
    print(b)

print()
#example-7 range from number1 to number2 and increase by number3
for c in range(3, 375, 5):
    print(c)

print()
#example-8 Else and else with break
for x5 in range(6):
  print(x5)
else:
  print("Finally finished!")

print()
for x6 in range(6):
    if x6 == 4:
        break
    print(x6)
else:
    print("Finally finished!")

print()
#example-9 Nested
adj = ["red", "big", "tasty"]
fruit = ["apple", "banana", "cherry"]

for n in adj:
  for m in fruits:
    print(n, m)

print()
#example-10 pass
for x7 in [0,1,2]:
    pass