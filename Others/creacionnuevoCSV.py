import pandas as pd
PlayerAttributes=pd.read_csv("C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\\Proyecto1\\Player_Attributes.csv")
PlayerSalary=pd.read_csv("C:\\Users\\raule\\Desktop\\CuartoSemestre2022\\BasedeDatos\Proyecto1\\Player_Salary.csv")
PlayerSalary= PlayerSalary.join(PlayerAttributes.set_index('DISPLAY_FIRST_LAST'), on='namePlayer')
print(PlayerSalary)
Salary=pd.DataFrame().assign(Season=PlayerSalary['slugSeason'],PlayerID=PlayerSalary['ID'],Contract_Type=PlayerSalary['typeContractDetail'],Value=PlayerSalary['value'])
Salary.to_csv('Salary.csv')
print(Salary)