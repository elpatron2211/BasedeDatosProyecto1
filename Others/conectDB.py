#Creacion de tablas e insercion de datos
import psycopg2
conn= psycopg2.connect(
    database="proyecto01",
    user='postgres',
    password='Manager123',
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
    Arena varchar(30),
    Arena_capacity int
    );'''
#Creando la tabla en la base de datos
cursor.execute(Team)
print('La tabla team fue creada exitosamente')
#Insertando el archivo csv en la tabla
Team='''Copy Team FROM
'C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Others\\TeamsTable.csv'
DELIMITER ',' CSV HEADER'''
#Ejecutando
cursor.execute(Team)
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
#Creando la tabla Player en la base de datos
cursor.execute(player)
print('Tabla Creada')
#Ingreso de datos en tabla Player
Player = '''Copy Official FROM 'C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Others\\PlayerTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Player)
print('Insertando Datos')

#Creacion de tabla Salary
salary='''Create Table Salary(
Season int primary key,
Player_ID int references Player(Player_ID),
Contract_Type varchar(10),
Value INT
);'''
#Creando la tabla salario en la base de datos
cursor.execute(salary)
print('Tabla Creada')
Salary = '''Copy Official FROM 'C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Others\\SalaryTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Salary)
print('Insertando Datos')

#Creacion de tabla oficial
Official='''Create Table Official(
Official_ID int primary key,
Full_Name varchar(30)
);
'''
cursor.execute(Official)
print('Tabla Creada')
# Insercion de datos de tabla de officiales
Official = '''Copy Official FROM 'C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Others\\OfficialsTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Official)
print('Insertando Datos')

Match = '''Create Table Match(
    Game_ID int,
    Season int,
    Game_Date VARCHAR(20),
    Visitor_ID VARCHAR(20) references Team(Team_ID),
    Home_ID VARCHAR(20) references Team(Team_ID),
    Attendace int,
    Home_Pts VARCHAR(6),
    Home_WL VARCHAR(3),
    FGM_Home VARCHAR(6),
    FGA_Home VARCHAR(6),
    FG_PCT_Home VARCHAR(6),
    FG3M_Home VARCHAR(6),
    FG3A_Home VARCHAR(6),
    FG3_PCT_Home VARCHAR(6),
    
    Primary key (Game_ID, Season)
)'''
# Insercion de datos de tabla de 
#Closing the connection
conn.close()