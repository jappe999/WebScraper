#import pymysql, re
#def connect_db():
#SELECT * FROM queue WHERE visited = 1 AND INDEXED NOT 1


import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port= 3306,
                             user='root',
                             password='42069blazeIt',
                             db='beta',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM queue WHERE visited = 1 AND indexed is NULL limit 20;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
