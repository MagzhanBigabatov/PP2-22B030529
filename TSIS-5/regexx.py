import re

#exercise-1
txt1 = input("First: ")
result1 = re.search('ab*', txt1)
if result1:
    #print(r)
    print("True")
else:
    print("No match")

#exercise-2
txt2 = input("Second: ")
result2 = re.search('ab{2}.{4}', txt2)
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
result5 = re.findall('[^a]+[b$]', txt5)
if result5:
    print("True")
else:
    print("No matches")

#exercise-6
txt6 = input("Sixth: ")
result6 = re.sub('[ ,.]', ":", txt6)
print(result6)

#exercise-7 разделяет строку на лист по _, затем объединяет все
list7 = list()
txt7 = input("Seventh: ")
pattern7 = re.split('_', txt7)
for i in pattern7:
    list7.append(i.capitalize())
result7 = "".join(list7)
print(result7)

#exercise-8 #делит строки которые связаны с заглавной
txt8 = input("Eighth: ")
result8 = re.split('[A-Z]', txt8)
print(result8)

#exercise-9 #добовляет пробел к словам начинающеимся с заглавной
txt9 = input("Nineth: ")
pattern9 = re.findall('[A-Z][a-z]*', txt9)
result9 = " ".join(pattern9)
print(result9)

#exercise-10 находит все строки у которых начало заглавная, затем объеденяет с _ и меняет заглавные на обычные 
txt10 = input("Tenth: ")
list10 = list()
pattern10 = re.findall('[A-Z][a-z]*', txt10)
for i in pattern10:
    list10.append(i.lower())
result10 = "_".join(list10)
print(result10)