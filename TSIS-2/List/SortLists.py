#examples
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#examples
thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)

#examples
thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist2.sort(reverse = True)
print(thislist2)

#examples
thislist3 = [100, 50, 65, 82, 23]
thislist3.sort(reverse = True)
print(thislist3)

#examples
def myfunc(n):
  return abs(n - 50)

thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(key = myfunc)
print(thislist4)

#examples
thislist5 = ["banana", "Orange", "Kiwi", "cherry"]
thislist5.sort()
print(thislist5)

#examples
thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.sort(key = str.lower)
print(thislist6)

#examples
thislist7 = ["banana", "Orange", "Kiwi", "cherry"]
thislist7.reverse()
print(thislist7)