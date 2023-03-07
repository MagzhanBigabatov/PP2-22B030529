import os

def writetext(name):
    file = open(name, 'w')
    file.writelines(input())
    file.close()

def appendtext(name):
    file = open(name, 'a')
    file.writelines(input())
    file.writelines('\n')
    file.close()
        


Filename = input("write file name: ")
choose = int(input())
if choose ==1:
    writetext(Filename)
if choose == 2:
    appendtext(Filename)