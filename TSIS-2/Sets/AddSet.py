thisset = {"apple", "banana", "cherry"}

#Example-1 adding element
thisset.add("orange")

print(thisset)

print()
#example-2 добавление одного сета на другой
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset) #"apple","pineapple", "banana","mango", "cherry","papaya"

print()
#example-3 можно добавлять лист, тупл на сет
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)