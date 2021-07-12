import mysql.connector

def conecta_chinook():
    conn = mysql.connector.connect (host=" ", port=" "
    , user=" ", passwd=" ", database="chinook")
    
    cursor = conn.cursor()
    
    return conn
