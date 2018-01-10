import mysql.connector
conn=mysql.connector.connect(user='root',password='asif',host='localhost')
mycrsr=conn.cursor()
mycrsr.execute("CREATE DATABASE python")

