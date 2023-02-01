#example-1 convert tuple to list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print()
#example-2 add by convert tuple to list, then again to tuple
thistuple = ("apple", "banana", "cherry")
y1 = list(thistuple)
y1.append("orange")
thistuple = tuple(y1)

print()
#example-3 add tuple in tuple
thistuple1 = ("apple", "banana", "cherry")
y2 = ("orange",)
thistuple1 += y2

print(thistuple1)

print()
#example-4 removing
thistuple2 = ("apple", "banana", "cherry")
y3 = list(thistuple2)
y3.remove("apple")
thistuple2 = tuple(y3)

print()
#deleting tuple
thistuple3 = ("apple", "banana", "cherry")
del thistuple3
print(thistuple3) #will be error, because tuple not exist