#exercise-1
def Mulp(list1):
    c=1
    for i in list1:
        c*=i
    return c

list1 = [1, 2, 5, 10]
print(Mulp(list1), end=" ")

#exercise-2
def check(str):
    lowerC =0
    upperC =0
    for i in str:
        if(i.islower()):
            lowerC+=1
        elif(i.isupper()):
            upperC+=1
    print("LowerCase letter:", lowerC)
    print("UpperCase letter:", upperC)

    
string = str(input("Write any sentence: "))
check(string)

#exercise-3
def Palindrome(str1):
    return str1 == str1[::-1]

string1 = str(input("Write any sentence: "))
if Palindrome(string1):
    print("Yes")
else:
    print("No")

#exercise-4
import math
def SqureRoot(num):
    return math.sqrt(num)

print("Sample Input:")
number = int(input())
mlsecond = int(input())
print("Sample Output:" "\n" "Square root of", number, "after",mlsecond,"miliseconds is", SqureRoot(number))

#exercise-5
tuple1 = (1, 5, 2)
print(all(tuple1))
