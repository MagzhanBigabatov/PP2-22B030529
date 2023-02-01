#example Dict can contain Dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

x = myfamily["child1"]
y = myfamily["child2"]
z = myfamily["child3"]
print(x)
print(y)
print(z)
