# hacer una funcion que recive los datos para hacer una regresion de un grupo en especifico
"""
Input: Tres o mas columnas de datos: datos cualitativos por año del groupo que se esta analizando y otros grupos de los cuales el grupo a analizar es dependiente; la razon de cambio del grupo a analizar
Proceso: Hacer la regresion, y automaticamente extraer los coefiicentes obtenidos del. modelo, de ahi construir la ecuacion diferencial, y hacer runge kutta
Output: una matriz con los datos del modelo hasta el anio deseado para la graficacion posterior.

Se asume que los datos ya estan limpios y preparados para su analisis
"""

import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from RK import RK4


def modelo_poblacion(t, y, model):
    jt, at, et = y
    dyJ = model.params.iloc[0] * at - model.params.iloc[1] * jt
    return dyJ


def modelacion(
    cols, dxdt, modelo, proj
):  # matriz de datos ordenados conforme a la definicion de la ecuacion
    x = cols
    y = dxdt
    modelo = sm.OLS(y, x).fit
    y0 = cols[0][0]
    t, y = RK4(modelo, y0, 0, proj, 0.01)
    return t, y
