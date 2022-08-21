import pandas as pd
#Creacion de tabla Salary
PlayerAttributes=pd.read_csv("C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\\Proyecto1\\Player_Attributes.csv")
PlayerSalary=pd.read_csv("C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\Proyecto1\\Player_Salary.csv")
PlayerSalary= PlayerSalary.join(PlayerAttributes.set_index('DISPLAY_FIRST_LAST'), on='namePlayer')
#print(PlayerSalary)
Salary=pd.DataFrame().assign(Season=PlayerSalary['slugSeason'],PlayerID=PlayerSalary['ID'],Contract_Type=PlayerSalary['typeContractDetail'],Value=PlayerSalary['value'])
Salary.to_csv('Salary.csv')
#print(Salary)
#Creacion de Tabla Team
TeamAttributes=pd.read_csv("C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\\Proyecto1\\Team_Attributes.csv")
Team=pd.read_csv("C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\\Proyecto1\\Team.csv")
TeamAttributes=TeamAttributes.join(Team.set_index('id'),on='ID')
Teams=pd.DataFrame().assign(Team_ID=TeamAttributes['ID'],Full_Name=TeamAttributes['full_name'],Abbreviation=TeamAttributes['abbreviation'],Nickname=TeamAttributes['NICKNAME'],City=TeamAttributes['CITY'],State=TeamAttributes['state'],Arena=TeamAttributes['state'])
Teams.to_csv("Teams.csv")
print(Teams)
