#Example-1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#example-2
a=375
b=33

if b>a:
    print("b is greater than a")
else:
    print("b is not greater thatn a")

print("\n")

#example-3
print(bool("Hello"))
print(bool(15))

print("\n")

#example-4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#False Values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print()

#Bool in class and func
#example-1
class myclass():
    def __len__(self):
        return 0

myjob = myclass()
print(bool(myjob))

#example-2
def myfunc():
    return True

print(myfunc())

#example-3
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")