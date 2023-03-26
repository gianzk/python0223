import pandas as pd
import os

dicx = {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth"
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }

# col -> n => cada columna tiene que tener m datos
# df -> es un Dataframe
df = pd.DataFrame(dicx)
print(df)

lista = [
            ["Rick", "Sanchez", 60],
            ["Morty", "Smith", 14]
        ]

# nombre de columnas
columnas= ["nombre", "apellido", "edad"]
df_rick_morty = pd.DataFrame(lista, columns = columnas) # psaando n argumentos por nombre
print(df_rick_morty)

urlabosulta="C:\\Users\\User\\Desktop\\courseWorkspace\\workspacepy0223\\python0223\\clase2603\\input\\primary_results.csv" #para mi pc
df=pd.read_csv(urlabosulta)

print(df)

df2=pd.read_csv('./clase2603/input/primary_results.csv')
print("here",df2)
print(os.path.dirname(__file__))
print(os.getcwd())


df2.to_csv('./clase2603/output/data_partidos.csv')