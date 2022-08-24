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
#db='''CREATE DATABASE proyecto01;
#'''
#cursor.execute(db)
#print('Database created succesfully')
#Create table Team
Team='''CREATE TABLE if not exists Team(
    Team_ID int primary key,
    Full_Name varchar(30),
    Abbreviation varchar(10),
    Nickname varchar(20),
    City varchar(20),
    State varchar(30),
    Arena varchar(30),
    Arena_capacity FLOAT,
    Coach_was_Player boolean
    );'''
#Creando la tabla en la base de datos
cursor.execute(Team)
print('Tabla team creada')
#Insertando el archivo csv en la tabla
Team='''Copy Team FROM
'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\Others\\TeamsTable.csv'
DELIMITER ',' CSV HEADER'''
#Ejecutando
cursor.execute(Team)
print('Insertados datos de team')

#Creacion de tabla oficial
Official='''Create Table if not exists Official(
Official_ID int primary key,
Full_Name varchar(30)
);
'''
cursor.execute(Official)
print('Tabla Creada oficial')
# Insercion de datos de tabla de officiales
Official = '''Copy Official FROM 'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\Others\\OfficialsTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Official)
print('Insertando Datos oficial')

#Create table Player
player='''Create Table if not exists Player(
   Player_ID int primary key,
   Full_Name VARCHAR(60),
   Height FLOAT,
   Weight FLOAT,
   Position VARCHAR(20),
   Team_ID int references Team(Team_ID) on delete cascade,
   Draft_year VARCHAR(10),
   Draft_round VARCHAR(10),
   Draft_number VARCHAR(10),
   Pts FLOAT,
   Ast FLOAT,
   Reb FLOAT,
   AllStarAppearances FLOAT,
   StatusPlayer VARCHAR(10)
);
'''
#Creando la tabla Player en la base de datos
cursor.execute(player)
print('Tabla Creada player')
#Ingreso de datos en tabla Player
Player = '''Copy Player FROM 'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\Others\\PlayerTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Player)
print('Insertando Datos player')

#Creacion de tabla Salary
salary='''Create Table if not exists Salary(
Season varchar(7),
Player_ID int references Player(Player_ID) on delete cascade,
Contract_Type varchar(20),
Value FLOAT,
Primary key (Season, Player_ID, Contract_Type, Value)
);'''
#Creando la tabla salario en la base de datos
cursor.execute(salary)
print('Tabla Creada Salary')
Salary = '''Copy Salary FROM 'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\Others\\SalaryTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Salary)
print('Insertando Datos Salary')

Match = '''Create Table if not exists Match(
    Game_ID int,
    Season int,
    Game_Date Date,
    Visitor_ID int references Team(Team_ID) on delete cascade,
    Home_ID int references Team(Team_ID) on delete cascade,
    Attendace FLOAT,
    Home_Pts VARCHAR(6),
    Home_WL VARCHAR(3),
    FGM_Home VARCHAR(6),
    FGA_Home VARCHAR(6),
    FG_PCT_Home VARCHAR(6),
    FG3M_Home VARCHAR(6),
    FG3A_Home VARCHAR(6),
    FG3_PCT_Home VARCHAR(6),
    FTM_Home VARCHAR(6),
    FTA_Home VARCHAR(6),
    FT_PCT_Home VARCHAR(6),
    OREB_Home VARCHAR(6),
    DREB_Home VARCHAR(6),
    REB_Home VARCHAR(6),
    AST_Home VARCHAR(6),
    BLK_Home VARCHAR(6),
    TOV_Home VARCHAR(6),
    Plus_Minus_Home VARCHAR(6),
    PF_Home VARCHAR(6),
    Visitor_Pts VARCHAR(6),
    Visitor_WL VARCHAR(3),
    FGM_Visitor VARCHAR(6),
    FGA_Visitor VARCHAR(6),
    FG_PCT_Visitor VARCHAR(6),
    FG3M_Visitor VARCHAR(6),
    FG3A_Visitor VARCHAR(6),
    FG3_PCT_Visitor VARCHAR(6),
    FTM_Visitor VARCHAR(6),
    FTA_Visitor VARCHAR(6),
    FT_PCT_Visitor VARCHAR(6),
    OREB_Visitor VARCHAR(6),
    DREB_Visitor VARCHAR(6),
    REB_Visitor VARCHAR(6),
    AST_Visitor VARCHAR(6),
    BLK_Visitor VARCHAR(6),
    TOV_Visitor VARCHAR(6),
    PF_Visitor VARCHAR(6),
    Plus_Minus_Visitor VARCHAR(6),
    Official_ID_1 int references Official(Official_ID) on delete cascade,
    Official_ID_2 int references Official(Official_ID) on delete cascade,
    Official_ID_3 int references Official(Official_ID) on delete cascade,
    Primary key (Game_ID, Season)
)'''
cursor.execute(Match)
print("Tabla creada juego")
Match = '''Copy Match FROM 'C:\\Users\\raule\\Documents\\GitHub\\BasedeDatosProyecto1\Others\\MatchTable.csv' DELIMITER ',' CSV HEADER'''
cursor.execute(Match)
# Insercion de datos de tabla de 
#Closing the connection

conn.close()