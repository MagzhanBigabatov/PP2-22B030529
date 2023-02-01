thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#example loop 
for x in thisdict:
    print(x) #print key one by one

print()

for x in thisdict:
    print(thisdict[x]) #print value

#example loop by use values(), will print values
for x in thisdict.values():
    print(x)

print()

for x in thisdict.keys():
    print(x) #will print Keys

print()
#example print keys and values
for x, y in thisdict.items():
    print(x, y)