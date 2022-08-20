#Proyecto01
#Diego Alonzo
#Paulo Sanchez
import psycopg2
#Defincion de conexion 
conn= psycopg2.connect(
    host="localhost",
    database="Proyecto01",
    user="postgres",
    password="sexoanal123"
)
#Realizar conexion
cur= conn.cursor()

#Finalizar conexion
conn.close()
