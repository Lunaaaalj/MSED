import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# === Cargar los datos ===
# Debe tener columnas: year, A, J, E, dA, dJ, dE
data = pd.read_csv("tus_datos.csv")

# Tomamos b(t) = 1
b = 1

# === Ecuaciones ===
# dJ/dt = b*A - mJ*J - (1/15)*J
#  => dJ/dt = b*A - J*(mJ + 1/15)
#  => mJ = (b*A - dJ/dt)/J - 1/15

data["mJ"] = (b * data["A"] - data["dJ"]) / data["J"] - 1 / 15

# dA/dt = (1/15)*J - mA*A - (1/50)*A
#  => mA = ((1/15)*J - dA/dt - (1/50)*A) / A
data["mA"] = ((1 / 15) * data["J"] - data["dA"] - (1 / 50) * data["A"]) / data["A"]

# dE/dt = (1/50)*A - mE*E
#  => mE = ((1/50)*A - dE/dt) / E
data["mE"] = ((1 / 50) * data["A"] - data["dE"]) / data["E"]

# === Mostrar resultados ===
print(data[["year", "mJ", "mA", "mE"]])

# Si deseas ajustar una regresión para ver cómo cambian con el tiempo:
X = data[["year"]]
for param in ["mJ", "mA", "mE"]:
    y = data[param]
    model = LinearRegression().fit(X, y)
    print(f"Regresión lineal para {param}:")
    print(f"  Intercepto: {model.intercept_:.5f}")
    print(f"  Pendiente: {model.coef_[0]:.5f}")
