#example-1 
thisset = {"apple", "banana", "cherry"}
print(thisset)

print()
#example-2 duplicate can not be 
thisset1 = {"apple", "banana", "cherry", "apple"}

print(thisset1) #will be "apple", "banana", "cherry"

print()
#example-3 length of set
print(len(thisset))

print()
#example data types and set can contain diff data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set4 = {"abc", 34, True, 40, "male"}

print(set1)
print(set2)
print(set3)
print()
print(type(set4)) #type of set
print(set4)

print()
#example-4
thisset2 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset2)