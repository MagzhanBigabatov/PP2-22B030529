import os
def create_file(file_n):
    file = open(f"{file_n}", 'x')
    file.close()
def existence_file(file_n):
    print('Exist:', os.access(f"{file_n}", os.F_OK))
    print('Readable:', os.access(f"{file_n}", os.R_OK))
    print('Writable:', os.access(f"{file_n}", os.W_OK))
    print('Executable:', os.access(f"{file_n}", os.X_OK))
def read_file(file_n):
    file = open(f"{file_n}", 'r')
    print(file.read())
    file.close()
def write_file(file_n):
    file = open(f"{file_n}", 'w')
    file.writelines(input())
    file.writelines('\n')
    file.close()
def append_file(file_n):
    file = open(f"{file_n}", 'a')
    file.writelines(input())
    file.writelines('\n')
    file.close()
def delete_file(file_n):
    os.remove(f"{file_n}")

file_name = input("write file name: ").strip()
choose = int(input("1) create" '\n' "2) check" '\n' "3) read" '\n' "4) write" '\n' "5) append" '\n' "6) delete" '\n'))
if choose == 1:
    create_file(file_name)
if choose == 2:
    existence_file(file_name)
if choose == 3:
    read_file(file_name)
if choose == 4:
    write_file(file_name)
if choose == 5:
    append_file(file_name)
if choose == 6:
    delete_file(file_name)