#example-1 For
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print()
#example-2 loop with range and len
for i in range(len(thistuple)):
    print(thistuple[i])

print()
#example-3 while 
thistuple1 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple1):
  print(thistuple1[i])
  i = i + 1