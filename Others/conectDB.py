from asyncio.windows_events import NULL
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

if __name__ == '__main__':    
    cursor = connectDB()
    # draftTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Draft.csv')
    # draftCombineTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Draft_Combine.csv')
    GameTable = pd.read_csv('Game.csv')
    # GameInactivePlayersTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Game_Inactive_Players.csv')
    GameOfficialsTable = pd.read_csv('Game_Officials.csv')
    # NewsTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\News.csv')
    # NewsMissingTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\News_Missing.csv')
    #                           C:\Users\Windows 10\Documents\UVG\CODING\Semestre 4\DB1\Proyectos\Datos\Datos
    PlayerTable = pd.read_csv("Player.csv")
    PlayerAttributesTable = pd.read_csv('Player_Attributes.csv')
    # PlayerBiosTable = pd.read_csv('Player_Bios.csv')
    # PlayerSalaryTable = pd.read_csv('Player_Salary.csv')
    # TeamTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team.csv')
    # TeamAttributesTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_Attributes.csv')
    # TeamHistoryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_History.csv')
    # TeamSalaryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_Salary.csv')
    Player = pd.DataFrame().assign(Player_ID = PlayerAttributesTable['ID'], Full_Name = PlayerTable['full_name'], Height = PlayerAttributesTable['HEIGHT'], Weight = PlayerAttributesTable['WEIGHT'], Team_ID = PlayerAttributesTable['TEAM_ID'], Draft_year = PlayerAttributesTable['DRAFT_YEAR'], Draft_round = PlayerAttributesTable['DRAFT_ROUND'], Draft_number = PlayerAttributesTable['DRAFT_NUMBER'], Pts = PlayerAttributesTable['PTS'], Ast = PlayerAttributesTable['AST'], Reb = PlayerAttributesTable['REB'], AllStarAppereances = PlayerAttributesTable['ALL_STAR_APPEARANCES'] )
    CopyGameOfficialsTable = pd.DataFrame(GameOfficialsTable)
    GameOfficialsTable = GameOfficialsTable.drop_duplicates(subset=['OFFICIAL_ID'])
    GameOfficialsTable['Full_Name'] = GameOfficialsTable['FIRST_NAME']+' '+GameOfficialsTable['LAST_NAME']
    Officials = pd.DataFrame().assign(Official_ID = GameOfficialsTable['OFFICIAL_ID'], Full_Name = GameOfficialsTable['Full_Name'])
    # print(CopyGameOfficialsTable.groupby("GAME_ID"))
    GameOfficials = pd.DataFrame().assign(First_Name = (CopyGameOfficialsTable.groupby(["GAME_ID"])["OFFICIAL_ID"]))
    GameID = []
    Of1 = []
    Of2 = []
    Of3 =[]
    for x in range(len(GameOfficials)):
        GameID.append(str(GameOfficials.loc[x][0][0]))
        Of1.append(str(GameOfficials.loc[x][0][1].iloc[0]))
        Of2.append(str(GameOfficials.loc[x][0][1].iloc[1]))
        try:
            Of3.append(str(GameOfficials.loc[x][0][1].iloc[2]))
        except:
            Of3.append(NULL)
    Match = pd.DataFrame().assign(Game_ID = GameTable['GAME_ID'], Season = GameTable['SEASON'], Game_Date = GameTable['GAME_DATE'], Visitor_ID = GameTable['VISITOR_TEAM_ID'], Home_ID = GameTable['HOME_TEAM_ID'], Attendance = GameTable['ATTENDANCE'], Home_Pts = GameTable['PTS_HOME'], Home_WL = GameTable['WL_HOME'], FGM_Home = GameTable['FGM_HOME'], FGA_Home = GameTable['FGA_HOME'], FG_PCT_Home = GameTable['FG_PCT_HOME'], OREB_Home = GameTable['OREB_HOME'], DREB_Home = GameTable['DREB_HOME'], REB_Home = GameTable['REB_HOME'], AST_Home = GameTable['AST_HOME'], BLK_Home = GameTable['BLK_HOME'], TOV_Home = GameTable['TOV_HOME'], PF_Home = GameTable['PF_HOME'], Plus_Minus_Home = GameTable['PLUS_MINUS_HOME'], Visitor_Pts = GameTable['PTS_AWAY'], Visitor_WL = GameTable['WL_AWAY'], FGM_Visitor = GameTable['FGM_AWAY'], FGA_Visitor = GameTable['FGA_AWAY'], FG_PCT_Visitor = GameTable['FG_PCT_AWAY'], OREB_Visitor = GameTable['OREB_AWAY'], DREB_VISITOR = GameTable['DREB_AWAY'], REB_Visitor = GameTable['REB_AWAY'], AST_Visitor = GameTable['AST_AWAY'], BLK_Visitor = GameTable['BLK_AWAY'], TOV_Visitor = GameTable['TOV_AWAY'], PF_Visitor = GameTable['PF_AWAY'], Plus_Minus_Visitor = GameTable['PLUS_MINUS_AWAY'])

    vacio = [NULL]*len(Match)
    Match['Official_ID_1']=vacio
    Match['Official_ID_2']=vacio
    Match['Official_ID_3']=vacio

    # for x in range(len(Match)):
    #     print(Match.loc[x]['GAME_ID'])
    

    
    # print(GameOfficials)
    disconnectDB(cursor)