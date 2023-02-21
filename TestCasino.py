import random
inp = 0


def Easy(wallet):
    RandEasy = random.randint(0 , 10)
    print('Choose how many you point you give: ')
    point = int(input())
    if point > wallet:
        print("You dont have enough moneys")
        WalletFunc()
    else:
        print('Print Number')
        while True:
            num = int(input())
            if num == RandEasy:
                wallet = wallet + (point*2)
                print("Congratulation"\
                    "Now you have:", wallet,"$"\
                        "You want continue or stop")
                print("1: Continue - Yes")
                print("2: stop - ")
                x1 = input()
                if x1 == 1:
                    Easy(wallet)
                elif x1 == 2:
                    Start(wallet)




def GameFunc():
    print('Choose Difficulties:')
    print("  1: Easy")
    print("  2: Medium")
    print("  3: Hard")
    dif = int(input())
    if dif == 1:
        Easy(wallet)
    elif dif == 2:
        print()
        #Medium()
    elif dif == 3:
        print()
        #Hard()
    #RandEasy = random.randint(0 , 10)
    #RandMed = random.randint(0, 100)
    #RandHard = random.randint(0, 1000)

def WalletFunc(wallet):
    if wallet == 0:
        print('Top up your wallet')
        inp = int(input())
        wallet = inp
        Start()
    else:
        GameFunc()
def Instruction():
    print('Hello in casino game.'\
        'in this gama, you need find random number.'\
        'if you find, you will win, else you will lose')

def Start(wallet):
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
    


wallet = 0
Start(wallet)

