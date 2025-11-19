# Crear CSV con tasas de cambio históricas (UF a USD y MXN a USD)
import pandas as pd

# Tasas históricas aproximadas (promedio anual)
tasas_cambio = {
    'ANIO': list(range(2005, 2020)),
    'UF_to_USD': [
        29.5,   # 2005
        31.2,   # 2006
        33.8,   # 2007
        35.1,   # 2008
        37.4,   # 2009
        40.3,   # 2010
        43.5,   # 2011
        44.2,   # 2012
        45.8,   # 2013
        47.1,   # 2014
        42.3,   # 2015
        38.9,   # 2016
        39.2,   # 2017
        40.5,   # 2018
        41.8    # 2019
    ],
    'MXN_to_USD': [
        0.0917,  # 2005
        0.0912,  # 2006
        0.0918,  # 2007
        0.0920,  # 2008
        0.0755,  # 2009
        0.0789,  # 2010
        0.0789,  # 2011
        0.0765,  # 2012
        0.0779,  # 2013
        0.0743,  # 2014
        0.0603,  # 2015
        0.0529,  # 2016
        0.0530,  # 2017
        0.0503,  # 2018
        0.0527   # 2019
    ]
}

df_tasas = pd.DataFrame(tasas_cambio)
df_tasas.to_csv('data/processed/turismo_ingresos/tasas_cambio.csv', index=False)
print("Archivo de tasas de cambio creado:")
print(df_tasas)