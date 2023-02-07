#examples
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#examples
for i in range(len(thislist)):
  print(thislist[i])

#examples 
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#examples
[print(x) for x in thislist]