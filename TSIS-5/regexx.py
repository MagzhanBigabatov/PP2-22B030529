import re

#exercise-1
txt1 = input("First: ")
pattern1 = r'ab*'
result1 = re.search(pattern1, txt1)
if result1:
    #print(r)
    print("True")
else:
    print("No match")

#exercise-2
txt2 = input("Second: ")
pattern2 = r'a(b){2-3}'
result2 = re.search(pattern2, txt2)
if result2:
    print("True")
else:
    print("No match")

#exercise-3
txt3 = input("Third: ")
pattern3 = r'[a-z]+_[a-z]+'
result3 = re.findall(pattern3, txt3)
print(result3)

#exercise-4
txt4 = input("Fourth: ")
pattern4 = r'[A-Z][a-z]+'
result4 = re.findall(pattern4, txt4)
print(result4)

#exercise-5
txt5 = input("Fifth: ")
pattern5 = r'a(.)*(b)'
result5 = re.findall(pattern5, txt5)
if result5:
    print("True")
else:
    print("No matches")

#exercise-6
txt6 = input("Sixth: ")
pattern6 = '[ ,.]'
result6 = re.sub(pattern6, ":", txt6)
print(result6)

#exercise-7
list7 = list()
txt7 = input("Seventh: ")
pattern7 = re.split('_', txt7)
for i in pattern7:
    list7.append(i.capitalize())
result7 = "".join(list7)
print(result7)

#exercise-8
txt8 = input("Eighth: ")
result8 = re.split('[A-Z]', txt8)
print(result8)

#exercise-9
txt9 = input("Nineth: ")
pattern9 = re.findall('[A-Z][a-z]*', txt9)
result9 = " ".join(pattern9)
print(result9)

#exercise-10
txt10 = input("Tenth: ")
list10 = list()
pattern10 = re.findall('[A-Z][a-z]*', txt10)
for i in pattern10:
    list10.append(i.lower())
result10 = "_".join(list10)
print(result10)