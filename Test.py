print("Give correct answer")
print("Which is the currency of Kazahstan?")
print("Name one of the President of kazahstan?")
print("What year Kazakhstan proclaim independence?")
corr1 = input()
corr2 = input()
corr3 = input()
num = 0
true = True
if corr1 == 'Tenge':
    num = 1
    if corr2 == "Nazarbaev" or corr2 == "Tokaev":
        num = 2
        if corr3 == 1991:
            num = 3
            print("Answer; " +  (num/3)*100 + "%" )
        else:
            print("Answer; " + (num/3)*100 + "%" )
    else:
        print("Answer; " + (num/3)*100 + "%" )
else:
    print("Answer: " + (num/3)*100 + "%" )
    