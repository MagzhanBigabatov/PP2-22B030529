import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345679",
    database = "suppliers"
)
connection.autocommit = True
cursor = connection.cursor()
sql = "CREATE DATABASE Test"
cursor.execute(sql)
cursor.close()
connection.close()