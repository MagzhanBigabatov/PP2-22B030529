import psycopg2
from config import host, user, password, data_base
connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = data_base
)

cursor = connection.cursor()
# Names = input("Person Name:\n")
# Phones = input("Person Phone:\n")

connection.autocommit = True
Add_person = """INSERT INTO score_table(
    score, levels) 
    VALUES('0','0');"""
cursor.execute(Add_person)
print("Person Added")

# Select = """SELECT Full_Name, Phone_Num FROM phonebook1 order by Full_Name"""
# cursor.execute(Select)
# print(cursor.fetchall())

cursor.close()
connection.close()