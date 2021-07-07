import mysql.connector

def conecta_chinook():
    conn = mysql.connector.connect (host="sd2021-1.ch4slymbqpkt.us-east-1.rds.amazonaws.com", port="3306"
    , user="admin", passwd="admin2021", database="chinook")
    
    cursor = conn.cursor()
    
    return conn