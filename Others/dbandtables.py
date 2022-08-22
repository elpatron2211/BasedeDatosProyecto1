#Creacion de tablas e insercion de datos
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
#Team='''Copy Team FROM
#'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\\OthersTeams.csv'
#DELIMITER ',' CSV HEADER'''
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
#Insertando archivo en la tabla Player
player='''Copy Player FROM
'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\\Others\\PlayerTable.csv'
DELIMITER ',' CSV HEADER;'''
#Creando la tabla Player en la base de datos
cursor.execute(player)
print('Informacion insertada')
#Creacion de tabla Salary
salary='''Create Table Salary(
Season int primary key,
Player_ID int references Player(Player_ID),
Contract_Type varchar(10),
Value INT
);'''
#Creando la tabla salario en la base de datos
#cursor.execute(salary)
#print('Tabla Creada')
#Ingreso de datos en tabla Salary



#Creacion de tabla oficial
oficial='''Create Table Official(
Official_ID int primary key,
Full_Name varchar(30)
);
'''
#cursor.execute(oficial)
#print('Tabla Creada')
#Closing the connection
#Ingreso de datos en Official

conn.close()