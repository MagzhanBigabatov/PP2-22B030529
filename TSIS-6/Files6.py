import os
import string

def generator_alh():
    list_alf = list(string.ascii_lowercase)
    return list_alf

file_name = generator_alh()
for i in file_name:
    file = open(f"{i}", 'x')
    file.close()
