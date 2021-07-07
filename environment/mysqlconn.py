import mysql.connector
import json

conn = mysql.connector.connect (host="sd2021-1.ch4slymbqpkt.us-east-1.rds.amazonaws.com", port="3306"
, user="admin", passwd="admin2021", database="chinook")

cursor = conn.cursor()
cursor.execute ("select * from genres")
records =  cursor.fetchall()

#print(cursor.column_names)
#print(records)

#lista = []
#for r in records:
#    lista.append(dict(zip(cursor.column_names,r)))
#    print(f"{r[0]}-{r[1]}")

lista = [dict(zip(cursor.column_names,x)) for x in records]

print(json.dumps(lista, indent=4))

