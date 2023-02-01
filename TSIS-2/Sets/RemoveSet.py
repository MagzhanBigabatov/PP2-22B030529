thisset = {"apple", "banana", "cherry"}

#example-1 removing element from set
thisset.remove("banana")

print(thisset)

print()
#example-2
thisset.discard("banana") #if removing element will not exixt Remove give error, but discard will not

print(thisset)

thisset.add("banana")
print()
#example-3 pop will remove random element, but with this method elelment can choose
x = thisset.pop()
print(x)

print(thisset)

print()
#example clearing set and deleting set
thisset.clear() #empty set
print(thisset)

print()
del thisset #set not exist
print(thisset)

