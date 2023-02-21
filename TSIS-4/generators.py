import math
#example 1
def generator1(n1):
    for i in range(n1+1):
        i*=i
        yield i
        

n1 = int(input())
for i in generator1(n1):
    print(i)

print()
#example 2
def generator2(n2):
    for i in range(n2+1):
        if i%2==0:
            yield i

n2 = int(input())
for i in generator2(n2):
    print(i)

print()
#example 3
def generator3(n3):
    for i in range(n3+1):
        if i%12==0:
            yield i
            
n3 = int(input())
for i in generator3(n3):
    print(i)

print()
#example 4
def generator4(a,b):
    for i in range(a , b):
        if math.sqrt(i) == int(math.sqrt(i)):
            yield i
            
a = int(input())
b = int(input())
for i in generator4(a,b):
    print(i)

print()
#example 5
def generator5(n5):
    for i in range(n5, 0 , -1):
        yield i

n5 = int(input())
for i in generator5(n5):
    print(i)