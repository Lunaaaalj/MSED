import pandas as pd
import statsmodels.api as sm

def regresion_mortalidad(df):
    df = df.copy()
    
    df['dJ/dt'] = df['J(t)'].diff()
    df['dA/dt'] = df['A(t)'].diff()
    df['dE/dt'] = df['E(t)'].diff()

    df = df.fillna(0)
    
    # Regresión Modelo Jóvenes (dJ/dt ~ J(t) + A(t))
    Y_j = df['dJ/dt']
    X_j = df[['J(t)', 'A(t)']]
    X_j = sm.add_constant(X_j, prepend=False)
    model_j = sm.OLS(Y_j, X_j).fit()
    coef_j = model_j.params.to_dict()

    # Regresión Modelo Mayores (dE/dt ~ A(t) + E(t))
    Y_e = df['dE/dt']
    X_e = df[['A(t)', 'E(t)']]
    X_e = sm.add_constant(X_e, prepend=False)
    model_e = sm.OLS(Y_e, X_e).fit()
    coef_e = model_e.params.to_dict()

    # Regresión Modelo Adultos (dA/dt ~ J(t) + A(t))
    Y_a = df['dA/dt']
    X_a = df[['J(t)', 'A(t)']]
    X_a = sm.add_constant(X_a, prepend=False)
    model_a = sm.OLS(Y_a, X_a).fit()
    coef_a = model_a.params.to_dict()

    resultados = {
        'modelo_jovenes': coef_j,
        'modelo_adultos': coef_a,
        'modelo_mayores': coef_e
    }
    
    return resultados, df