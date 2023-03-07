import os

FileName = input()
print(os.path.isdir(FileName))
checkfile = os.listdir(FileName)
text = '\n'.join(checkfile)
print(text)