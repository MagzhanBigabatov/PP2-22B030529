#example-1
price = 199.99
txt = "The price of the bread {:.2f} dollars"
print(txt.format(price))

#Multiple Values
#example-2

quantity = 3
itemno = 333
price = 33.3
myorder = "I want '\{} from 10'\ pieces of item number {} for {:.1f} dollars."
print(myorder.format(quantity, itemno, price))
