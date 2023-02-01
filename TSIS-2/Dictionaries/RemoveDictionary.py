thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#example delete element by key
thisdict.pop("model")
print(thisdict)

print()
#example delete last element
thisdict.popitem()
print(thisdict)

print()
#example delete by del
del thisdict["brand"]
print(thisdict)

#example dict can be deleted completely
del thisdict 

print()
#example clearing Dict
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.clear()
print(thisdict1)