#example-1
x1="World"

def myfunc1():
    print("Hello" + x1)

myfunc1()

#example-2
x2="World"

def myfunc2():
    x2="Moon"
    print("Hello" + x2)
myfunc2()

print("Hello" + x2)

#the global keyword

#example-1
def myfunc3():
    global x3
    x3 = "World"
myfunc3()

print("Hello" + x3)

#example-2
x4="World"

def myfunc4():
    global x4
    x4 = "Moon"
myfunc4()

print("Hello" + x4)