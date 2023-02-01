import random
#Exapmle-1
print("Example-1")
i=1
while i< 6:
    print(i)
    i+=1

print()
#Exapmle-2
print("Example-2")
i1 = 1
while i1<6:
    print(i1)
    if i1 == 3:
        break
    i1 += 1

print()
#Exapmle-3
print("Example-3")
i2 = 1 
while i2<6:
    i2 += 1
    if i2 == 3:
        continue
    print(i2)

print()
#Exapmle-4
print("Example-4")
i3=7
while i3<6:
    print(i3)
    i3+=1
else:
    print("I is not less 6")

print()
#Exercise:
print("Exercise:")
i4=1
while i4<6:
    print(i4)
    i4+=1

print()
#My Example
print("My Example")
count = 0
x = int()
num = random.randint(0 , 10)
print(num)
while x>=0 and x<=10:
    x = int(input())
    if x == num and count <= 5:
        print("Congra")
        break
    elif x== num and count > 5:
        print('Correct, but you lose')
        break
    elif count >= 10:
        print("Sorry you lose")
        break
    elif x!= num:
        count+=1
        continue
else:
    print("Why this number: " + str(x))


