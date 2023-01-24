#incorrect example

#age = 36
#txt = "My name is John, I am " + age
#print(txt)

#correct
age = "36"
txt = "My name is John, I am " + age
print(txt)

#or 

age1 = "36"
txt1 = "My name is John, I am {}" 
print(txt.format(age))

#example-2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#example-3
quantity1 = 3
itemno1 = 567
price1 = 49.95
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity1, itemno1, price1))

