set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

#example-1 объединение двух сетов в один
set3 = set1.union(set2)
print(set3)

print()
#example-2 добавляет один сет в другой
set1.update(set2)
print(set1)

print()
#example-3 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) #will show only duplicate element "Apple"

print()
#example-4 can be like this
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

z = x1.intersection(y1)

print(z)

print()
#example will show not Duplicate
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}

x2.symmetric_difference_update(y2)

print(x2)

print()
#example can be like this
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}

z2 = x3.symmetric_difference(y3)

print(z2)