#example-1 print by index, and can be negative index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print()
print(thistuple[-1])

print()
#example-2 range by index
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[2:5])
print()
print(thistuple1[:4]) #print from 0 to 4 index
print()
print(thistuple1[2:]) #print from 2 to the last index

print()
print()

print(thistuple1[-4: -1]) #print by negative index

print()
#example-3 tuple with if
thistuple2 = ("apple", "banana", "cherry")
if "apple" in thistuple2:
  print("Yes, 'apple' is in the fruits tuple") 


