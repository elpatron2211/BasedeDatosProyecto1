import psycopg2
conn= psycopg2.connect(
    database="proyecto01",
    user='postgres',
    password='hola123',
    host='localhost',
    port='5432'
)
conn.autocommit=True
#Creating curso
cursor=conn.cursor()
#Create database 
#db='''CREATE DATABASE proyecto01;
#'''
#cursor.execute(db)
#print('Database created succesfully')
#Create table Team
Team='''CREATE TABLE Team(
    Team_ID int primary key,
    Full_Name varchar(30),
    Abbreviation varchar(10),
    Nickname varchar(20),
    City varchar(20),
    State varchar(30),
    Arena varchar(30)
    );'''
#Creando la tabla en la base de datos
#cursor.execute(Team)
#print('La tabla team fue creada exitosamente')
#Insertando el archivo csv en la tabla
Team='''Copy Team FROM
'C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\\Proyecto1\\Archivos\\Teams.csv'
DELIMITER ',' CSV HEADER'''
#Ejecutando
#cursor.execute(Team)
#print('Insertando los datos')
#Comprobando la tabla team
#cursor.execute('select * from Team')
#Create table Player
player='''Create Table Player(
   Player_ID int primary key,
    Full_Name VARCHAR(60),
   Height int,
    Weight int,
   Position VARCHAR(10),
   Team_ID int references Team(Team_ID),
   Draft_year int,
   Draft_round int,
   Draft_number int,
   Pts Float,
   Ast Float,
   Reb Float,
   AllStarAppearances int
);'''
#Creando la tabla en la base de datos
#cursor.execute(player)
#print('Tabla Creada')
#Ingreso de datos en tabla Player


#Creacion de tabla Salary

#Clssing the connection
conn.close()