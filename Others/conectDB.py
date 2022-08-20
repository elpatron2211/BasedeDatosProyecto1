import psycopg2
import pandas as pd
def connectDB():
    conn = psycopg2.connect( database="Proyecto1", host = "localhost", user = "postgres", password = "Manager123", port = "5432" )
    print("Conexion realizada exitosamente")
    cursor = conn.cursor()
    return cursor

def disconnectDB(cursor): 
    cursor.close()
    print("Se cerro la conexion exitosamente")

def connectCSV(direccion):
    draftTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Draft.csv')
    draftCombineTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Draft_Combine.csv')
    GameTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Game.csv')
    GameInactivePlayersTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Game_Inactive_Players.csv')
    GameOfficialsTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Game_Officials.csv')
    NewsTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\News.csv')
    NewsMissingTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\News_Missing.csv')
    PlayerTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Player.csv')
    PlayerAttributesTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Player_Attributes.csv')
    PlayerBiosTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Player_Bios.csv')
    PlayerSalaryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Player_Salary.csv')
    TeamTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team.csv')
    TeamAttributesTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_Attributes.csv')
    TeamHistoryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_History.csv')
    TeamSalaryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_Salary.csv')
    return draftTable, draftCombineTable, GameTable, GameInactivePlayersTable, GameOfficialsTable,NewsMissingTable, NewsTable, PlayerAttributesTable, PlayerBiosTable, PlayerAttributesTable, PlayerTable, PlayerSalaryTable, TeamTable, TeamAttributesTable, TeamHistoryTable, TeamSalaryTable
if __name__ == '__main__':
    cursor = connectDB()
    arr = connectCSV()
    disconnectDB(cursor)