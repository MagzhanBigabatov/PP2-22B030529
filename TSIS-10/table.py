import psycopg2
from config import host, user, password, data_base
connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = data_base
)

cursor = connection.cursor()
Names = input("Person Name:\n")
Phones = input("Person Phone:\n")

connection.autocommit = True
Add_person = """INSERT INTO phonebook1(
    Full_Name, Phone_Num) 
    VALUES(%s, %s);"""
cursor.execute(Add_person, (Names, Phones,))
print("Person Added")

Select = """SELECT Full_Name, Phone_Num FROM phonebook1 order by Full_Name"""
cursor.execute(Select)
print(cursor.fetchall())

cursor.close()
connection.close()