# Limpieza de la base de datos
import pandas as pd
import numpy as np

df = pd.read_csv(  # Lectura de datos
    "../data/BBDD Población Chile (1b).xlsx - Tabla ajustada población .csv",
)


df = df.T  # Transposicion

# notacion europea a float
for col in df.columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

df = df.apply(pd.to_numeric, errors="ignore")


df = df.replace(["NaN", "nan", "NAN", "None", ""], np.nan)

df = df.fillna(0)

print(df)

df.to_csv("../data/output.csv")
