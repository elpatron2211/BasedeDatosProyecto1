from asyncio.windows_events import NULL
import psycopg2
import pandas as pd
def connectDB():
    conn = psycopg2.connect( database="proyecto01", host = "localhost", user = "postgres", password = "Manager123", port = "5432" )
    print("Conexion realizada exitosamente")
    cursor = conn.cursor()
    return cursor

def disconnectDB(cursor): 
    cursor.close()
    print("Se cerro la conexion exitosamente")

if __name__ == '__main__':    
    cursor = connectDB()
    PlayerTable = pd.read_csv("Others\\Player.csv")
    PlayerAttributesTable = pd.read_csv('Others\\Player_Attributes.csv')
    TeamAttributes=pd.read_csv('Others\\Team_Attributes.csv')
    Team=pd.read_csv('Others\\Team.csv')
    TeamAttributes=TeamAttributes.join(Team.set_index('id'),on='ID')
    Coach_Was_Player = [False]*len(TeamAttributes)
    Teams=pd.DataFrame().assign(Team_ID=TeamAttributes['ID'],Full_Name=TeamAttributes['full_name'],Abbreviation=TeamAttributes['abbreviation'],Nickname=TeamAttributes['NICKNAME'],City=TeamAttributes['CITY'],State=TeamAttributes['state'],Arena=TeamAttributes['ARENA'], Arena_Capacity = TeamAttributes['ARENACAPACITY'], Coach_was_Player = Coach_Was_Player)
    Teamwithcoachplayer = TeamAttributes.loc[TeamAttributes['HEADCOACH'].isin(PlayerTable.loc[:,'full_name'].tolist())]
    for x in range(len(TeamAttributes)):
        try:
            PlayerTable.loc[:,'full_name'].tolist().index(TeamAttributes['HEADCOACH'][x])
            Teams.loc[x,'Coach_was_Player'] = True
            # print("Hola")
        except:
            pass
    print(Teams)
    # draftTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Draft.csv')
    # draftCombineTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Draft_Combine.csv')
    GameTable = pd.read_csv('Others\\Game.csv')
    # GameInactivePlayersTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Game_Inactive_Players.csv')
    GameOfficialsTable = pd.read_csv('Others\\Game_Officials.csv')
    # NewsTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\News.csv')
    # NewsMissingTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\News_Missing.csv')
    #                           C:\Users\Windows 10\Documents\UVG\CODING\Semestre 4\DB1\Proyectos\Datos\Datos
    
    # PlayerBiosTable = pd.read_csv('Player_Bios.csv')
    PlayerSalaryTable = pd.read_csv('Others\\Player_Salary.csv')
    PlayerSalaryTable= PlayerSalaryTable.join(PlayerAttributesTable.set_index('DISPLAY_FIRST_LAST'), on='namePlayer')
    #print(PlayerSalary)
    Salary=pd.DataFrame().assign(Season=PlayerSalaryTable['slugSeason'],Player_ID=PlayerSalaryTable['ID'],Contract_Type=PlayerSalaryTable['typeContractDetail'],Value=PlayerSalaryTable['value'])
    
    # TeamTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team.csv')
    # TeamAttributesTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_Attributes.csv')
    # TeamHistoryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_History.csv')
    # TeamSalaryTable = pd.read_csv('C:\\Users\\Windows 10\\Documents\\UVG\\CODING\\Semestre 4\\DB1\\Proyectos\\Proyecto1\\Datos\\Datos\\Team_Salary.csv')
    Player = pd.DataFrame().assign(Player_ID = PlayerAttributesTable['ID'], Full_Name = PlayerTable['full_name'], Height = PlayerAttributesTable['HEIGHT'], Weight = PlayerAttributesTable['WEIGHT'], Position = PlayerAttributesTable['POSITION'], Team_ID = PlayerAttributesTable['TEAM_ID'], Draft_year = PlayerAttributesTable['DRAFT_YEAR'], Draft_round = PlayerAttributesTable['DRAFT_ROUND'], Draft_number = PlayerAttributesTable['DRAFT_NUMBER'], Pts = PlayerAttributesTable['PTS'], Ast = PlayerAttributesTable['AST'], Reb = PlayerAttributesTable['REB'], AllStarAppereances = PlayerAttributesTable['ALL_STAR_APPEARANCES'] )
    # print(Teams.loc[:,'Team_ID'].tolist())
    print(Player)
    Player = Player.loc[Player['Team_ID'].isin(Teams.loc[:,'Team_ID'].tolist())]
    print(Player)
    # Player.replace('None', NULL)
    # print(Player.loc[0:20,'Draft_year'])
    CopyGameOfficialsTable = pd.DataFrame(GameOfficialsTable)
    GameOfficialsTable = GameOfficialsTable.drop_duplicates(subset=['OFFICIAL_ID'])
    GameOfficialsTable['Full_Name'] = GameOfficialsTable['FIRST_NAME']+' '+GameOfficialsTable['LAST_NAME']
    Officials = pd.DataFrame().assign(Official_ID = GameOfficialsTable['OFFICIAL_ID'], Full_Name = GameOfficialsTable['Full_Name'])
    
    Salary = Salary.loc[(Salary['Player_ID'].isin(Player.loc[:, 'Player_ID'].tolist()))]
    Salary['Player_ID'] = Salary['Player_ID'].astype(int)
    Match = pd.DataFrame().assign(Game_ID = GameTable['GAME_ID'], Season = GameTable['SEASON'], Game_Date = GameTable['GAME_DATE'], Visitor_ID = GameTable['VISITOR_TEAM_ID'], Home_ID = GameTable['HOME_TEAM_ID'], Attendance = GameTable['ATTENDANCE'], Home_Pts = GameTable['PTS_HOME'], Home_WL = GameTable['WL_HOME'], FGM_Home = GameTable['FGM_HOME'], FGA_Home = GameTable['FGA_HOME'], FG_PCT_Home = GameTable['FG_PCT_HOME'], FG3M_Home = GameTable['FG3M_HOME'], FG3A_Home = GameTable['FG3A_HOME'], FG3_PCT_Home = GameTable['FG3_PCT_HOME'], FTM_Home = GameTable['FTM_HOME'], FTA_Home = GameTable['FTA_HOME'], FT_PCT_Home = GameTable['FT_PCT_HOME'], OREB_Home = GameTable['OREB_HOME'], DREB_Home = GameTable['DREB_HOME'], REB_Home = GameTable['REB_HOME'], AST_Home = GameTable['AST_HOME'], BLK_Home = GameTable['BLK_HOME'], TOV_Home = GameTable['TOV_HOME'], PF_Home = GameTable['PF_HOME'], Plus_Minus_Home = GameTable['PLUS_MINUS_HOME'], Visitor_Pts = GameTable['PTS_AWAY'], Visitor_WL = GameTable['WL_AWAY'], FGM_Visitor = GameTable['FGM_AWAY'], FGA_Visitor = GameTable['FGA_AWAY'], FG_PCT_Visitor = GameTable['FG_PCT_AWAY'], FG3M_Visitor = GameTable['FG3M_AWAY'], FG3A_Visitor = GameTable['FG3A_AWAY'], FG3_PCT_Visitor = GameTable['FG3_PCT_AWAY'], FTM_Visitor = GameTable['FTM_AWAY'], FTA_Visitor = GameTable['FTA_AWAY'], FT_PCT_Visitor = GameTable['FT_PCT_AWAY'], OREB_Visitor = GameTable['OREB_AWAY'], DREB_VISITOR = GameTable['DREB_AWAY'], REB_Visitor = GameTable['REB_AWAY'], AST_Visitor = GameTable['AST_AWAY'], BLK_Visitor = GameTable['BLK_AWAY'], TOV_Visitor = GameTable['TOV_AWAY'], PF_Visitor = GameTable['PF_AWAY'], Plus_Minus_Visitor = GameTable['PLUS_MINUS_AWAY'])
    vacio = [NULL]*len(Match)
    Match['Official_ID_1']=vacio
    Match['Official_ID_2']=vacio
    Match['Official_ID_3']=vacio
    GameOfficials = pd.DataFrame().assign(First_Name = (CopyGameOfficialsTable.groupby(["GAME_ID"])["OFFICIAL_ID"]))
    for x in range(len(GameOfficials)):
        try:
            index = int(Match.index[Match['Game_ID'] == GameOfficials.loc[x][0][0]].tolist()[0])
            Match['Official_ID_1'][index] = int(GameOfficials.loc[x][0][1].iloc[0])
            Match['Official_ID_2'][index] = int(GameOfficials.loc[x][0][1].iloc[1])
            Match['Official_ID_3'][index] = int(GameOfficials.loc[x][0][1].iloc[2])
        except:
            pass
    
    # print(Match)
    disconnectDB(cursor)
Match = Match.loc[(Match['Visitor_ID'].isin(Teams.loc[:,'Team_ID'].tolist())) & (Match['Home_ID'].isin(Teams.loc[:,'Team_ID'].tolist())) & (Match['Game_Date']>='2015-01-01')  & (Match['Official_ID_1'].isin(Officials.loc[:,'Official_ID'].tolist() )) & (Match['Official_ID_2'].isin(Officials.loc[:,'Official_ID'].tolist() )) & (Match['Official_ID_3'].isin(Officials.loc[:,'Official_ID'].tolist() )) ]
# Match = Match.loc[Match['Game_Date']>='2015-01-01']
print(Match)
Teams.to_csv("Others\\TeamsTable.csv", index=False)
Player.to_csv('Others\\PlayerTable.csv', index = False)
Officials.to_csv('Others\\OfficialsTable.csv', index = False)
Match.to_csv('Others\\MatchTable.csv', index = False)
Salary.to_csv('Others\\SalaryTable.csv', index = False)
print("Ya")
