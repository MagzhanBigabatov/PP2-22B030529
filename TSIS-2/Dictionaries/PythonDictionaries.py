thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#example print all dict
print(thisdict)

print()
#example print element by key
print(thisdict["brand"])

print()
#example in Dict can not be duplicates
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict1)

print()
#example Length
print(len(thisdict))

print()
#example in Dict can be any data type
thisdict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict2)

print()
#example type 
print(type(thisdict))

#example constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)