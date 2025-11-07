# Limpieza de la base de datos
import pandas as pd

df = pd.read_csv(
    "../data/BBDD Población Chile (1b).xlsx - Tabla ajustada población .csv"
)

df = df.T

print(df)
