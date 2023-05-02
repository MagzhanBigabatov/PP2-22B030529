import psycopg2
from config import host, user, password, data_base

try:
    connection = psycopg2.connect(
        host = host,
        user = user, 
        password = password,
        database = data_base
    )

    
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE score_table(
        id SERIAL PRIMARY KEY,
        score INT,
        levels INT
        );""")
        print("Table Created")
        connection.commit()

except Exception as ex:
    print(ex)
finally:
    connection.close()