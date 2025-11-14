import pandas as pd

df = pd.read_csv("data/output.csv")

df["tasa_rel_jovenes"] = df["dJ"] / df["Población total de jovenes (0-14)"]
df["tasa_rel_adultos"] = df["dA"] / df["Población total de adultos (15-64)"]
df["tasa_rel_mayores"] = df["dM"] / df["Poblacion total mayores (65+ años)"]

df[["tasa_rel_jovenes", "tasa_rel_adultos", "tasa_rel_mayores"]].head()

import statsmodels.api as sm

df["Año"] = df.index + 2002

X = sm.add_constant(df["Año"])
Y = df["tasa_rel_jovenes"]

modelo_mayores = sm.OLS(Y, X).fit()
print(modelo_mayores.summary())
