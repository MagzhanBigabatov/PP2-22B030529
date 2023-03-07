import os

def writetext(name1, name2):
    files2 = open(name2, 'a')
    files1 = open(name1, 'r')
    for line in files1:
        files2.writelines(line)
        files2.close()

def appendtext(name1, name2):
    files2 = open(name2, 'a')
    files1 = open(name1, 'r')
    for line in files1:
        files2.writelines(line)
        files2.writelines('\n')
        files2.close()
        


Filename1 = input("write first file name: ")
Filename2 = input("write second file name: ")
choose = int(input())
if choose ==1:
    writetext(Filename1, Filename2)
if choose == 2:
    appendtext(Filename1, Filename2)