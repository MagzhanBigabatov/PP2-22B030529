#examples
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#examples
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)

#examples
newlist2 = [x for x in fruits if x != "apple"]

#examples 
newlist3 = [x for x in fruits]

#examples
newlist4 = [x for x in range(10)]

#examples
newlist5 = [x for x in range(10) if x < 5]

#examples
newlist6 = [x.upper() for x in fruits]

#examples
newlist7 = ['hello' for x in fruits]

#examples
newlist8 = [x if x != "banana" else "orange" for x in fruits]