#example-1 присвоение значений к другим значениям 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print()
#example-2 if variables less than tuple, use asterisk
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)

print()
#asterisk  can be in any position
(green, *yellow, red) = fruits1

print(green)
print(yellow)
print(red)
