thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#example print by key
x = thisdict["model"]
print(x)
#example same result
x = thisdict.get("model")
print(x)

print()
#example print all keys in Dict
x1 = thisdict.keys()
print(x1)

print()
#example can add new element
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
} 

x1 = car.keys()

print(x1) #before the change

car["color"] = "white"

print(x1) #after the change

print()
#example will print all values in Dict
x = thisdict.values()

print()
#example 
car1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x2 = car1.values()

print(x2) #before the change

car1["year"] = 2020

print(x2) #after the change

print()
#example list of the key and value pairs
x = thisdict.items()

print()
#example 
car2 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x3 = car2.items()
print(x3) #before the change

car2["year"] = 2020
print(x3) #after the change

print()
#example
x4 = car2.items()
print(x4) #before the change

car2["color"] = "red"
print(x4) #after the change

print()
#exaple find with if 
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

