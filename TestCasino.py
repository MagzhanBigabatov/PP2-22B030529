import random
wallet = 0
def Easy(wallet):
    RandEasy = random.randint(0 , 10)
    print('Choose how many you point you give: ')
    point = int(input())
    if point > wallet:
        return WalletFunc()
    else:
        print('Print Number')
        true = True
        while true:
            num = int(input())
            if()




def GameFunc():
    print('Choose Difficulties:')
    print("  1: Easy")
    print("  2: Medium")
    print("  3: Hard")
    dif = int(input())
    if dif == 1:
        Easy(wallet)
    elif dif == 2:
        Medium()
    elif dif == 3:
        Hard()
    RandEasy = random.randint(0 , 10)
    RandMed = random.randint(0, 100)
    RandHard = random.randint(0, 1000)

def WalletFunc():
    if wallet == 0:
        print('Top up your wallet')
        inp = int(input())
    else:
        GameFunc()
def Instruction():
    print('Hello in casino game.'\
        'in this gama, you need find random number.'\
        'if you find, you will win, else you will lose')

print("1: Start game")
print("2: Instruction")
print("3: Exit")
var = int(input())

if var == 1:
    WalletFunc()
elif var == 2:
    Instruction()
elif var == 3:
    print('Good Bye') 