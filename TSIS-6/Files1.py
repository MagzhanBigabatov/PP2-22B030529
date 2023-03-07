import os

file1 = open("1text.txt", "w")
text1 = os.listdir(r"C:\Users\375_a\OneDrive\Desktop\c++\Python\HW-py\TSIS-6")
WriteText = '\n'.join(text1)
file1.write(WriteText)
file1.close()
