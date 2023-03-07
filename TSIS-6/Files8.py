import os
def delete(file):
    os.remove(file)

file_name = input()
if os.path.exists(file_name):
    delete(file_name)
else:
    print("file not exist")