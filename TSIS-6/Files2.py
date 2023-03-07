import os

print('Exist:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\1text.txt', os.F_OK))
print('Readable:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\1text.txt', os.R_OK))
print('Writable:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\1text.txt', os.W_OK))
print('Executable:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\1text.txt', os.X_OK))
print()
print('Exist:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\2text.txt', os.F_OK))
print('Readable:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\2text.txt', os.R_OK))
print('Writable:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\2text.txt', os.W_OK))
print('Executable:', os.access('C:\\Users\\375_a\\OneDrive\\Desktop\\c++\\Python\\HW-py\\TSIS-6\\2text.txt', os.X_OK))