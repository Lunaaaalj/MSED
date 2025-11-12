import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .funciones import rk4_sistemaEC

def simulacion(b_func, tasas_mortalidad, poblacion_inicial, t_inicial=2025, t_final=2050, h=1):
    u0 = np.array([
        poblacion_inicial['J'], 
        poblacion_inicial['A'], 
        poblacion_inicial['E']
    ])

    t0_relativo = 0
    t_final_relativo = t_final - t_inicial

    coef_j = tasas_mortalidad['modelo_jovenes']
    coef_a = tasas_mortalidad['modelo_adultos']
    coef_e = tasas_mortalidad['modelo_mayores']

    def funcion_demografica_regresion(t_rel, z):
        J = z[0]
        A = z[1]
        E = z[2]
        

        dJ_dt = (coef_j['J(t)'] * J) + (coef_j['A(t)'] * A) + coef_j['const']
        dA_dt = (coef_a['J(t)'] * J) + (coef_a['A(t)'] * A) + coef_a['const']
        dE_dt = (coef_e['A(t)'] * A) + (coef_e['E(t)'] * E) + coef_e['const']
        
        return np.array([dJ_dt, dA_dt, dE_dt])


    function = funcion_demografica_regresion
    
    U, T_relativo = rk4_sistemaEC(function, t0_relativo, t_final_relativo, u0, h)
    
    T_real = T_relativo + t_inicial
    
    return T_real, U


def generar_reporte(años_chile, y_chile, años_mexico, y_mexico):
    """
    Imprime los resultados numéricos de AMBOS países y luego
    genera la gráfica comparativa 2x2.
    (Esta función no requiere cambios)
    """
    
    print(f"\n=============================================")
    print(f" RESULTADOS: CHILE")
    print(f"=============================================")
    
    pob_inicial_cl = y_chile[0].sum()
    pob_final_cl = y_chile[-1].sum()
    crecimiento_total_cl = pob_final_cl - pob_inicial_cl
    crecimiento_porc_cl = (crecimiento_total_cl / pob_inicial_cl) * 100
    
    print(f"Población {int(años_chile[0])}: {pob_inicial_cl:,.0f}")
    print(f"Población {int(años_chile[-1])}: {pob_final_cl:,.0f}")
    print(f"Crecimiento Total: {crecimiento_total_cl:,.0f} ({crecimiento_porc_cl:.2f}%)")
    
    print("\n--- Desglose por Edad ---")
    print(f"           {int(años_chile[0])} \t\t {int(años_chile[-1])}")
    print(f"Jóvenes:   {y_chile[0, 0]:,.0f} \t {y_chile[-1, 0]:,.0f}")
    print(f"Adultos:   {y_chile[0, 1]:,.0f} \t {y_chile[-1, 1]:,.0f}")
    print(f"Mayores:   {y_chile[0, 2]:,.0f} \t {y_chile[-1, 2]:,.0f}")

    print(f"\n=============================================")
    print(f" RESULTADOS: MÉXICO")
    print(f"=============================================")
    
    pob_inicial_mx = y_mexico[0].sum()
    pob_final_mx = y_mexico[-1].sum()
    crecimiento_total_mx = pob_final_mx - pob_inicial_mx
    crecimiento_porc_mx = (crecimiento_total_mx / pob_inicial_mx) * 100

    print(f"Población {int(años_mexico[0])}: {pob_inicial_mx:,.0f}")
    print(f"Población {int(años_mexico[-1])}: {pob_final_mx:,.0f}")
    print(f"Crecimiento Total: {crecimiento_total_mx:,.0f} ({crecimiento_porc_mx:.2f}%)")
    
    print("\n--- Desglose por Edad ---")
    print(f"           {int(años_mexico[0])} \t\t {int(años_mexico[-1])}")
    print(f"Jóvenes:   {y_mexico[0, 0]:,.0f} \t {y_mexico[-1, 0]:,.0f}")
    print(f"Adultos:   {y_mexico[0, 1]:,.0f} \t {y_mexico[-1, 1]:,.0f}")
    print(f"Mayores:   {y_mexico[0, 2]:,.0f} \t {y_mexico[-1, 2]:,.0f}")
    print(f"=============================================\n")

    
    fig, axes = plt.subplots(2, 2, figsize=(18, 14))
    fig.suptitle('Proyección Demográfica Comparativa (2025-2050)', fontsize=20, fontweight='bold')
    plt.subplots_adjust(hspace=0.35, wspace=0.25)

    # Formateador para millones
    formatter = plt.FuncFormatter(lambda x, p: f'{x/1_000_000:.1f}M')

    # Gráfica 1: Chile
    ax1 = axes[0, 0]
    ax1.plot(años_chile, y_chile[:, 0], 'b-', linewidth=2, label='Jóvenes (0-14)')
    ax1.plot(años_chile, y_chile[:, 1], 'g-', linewidth=2, label='Adultos (15-64)')
    ax1.plot(años_chile, y_chile[:, 2], 'r-', linewidth=2, label='Mayores (65+)')
    ax1.set_xlabel('Año', fontsize=12)
    ax1.set_ylabel('Población', fontsize=12)
    ax1.yaxis.set_major_formatter(formatter)
    ax1.set_title('CHILE: Proyección Demográfica', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    # Gráfica 2: México
    ax2 = axes[0, 1]
    ax2.plot(años_mexico, y_mexico[:, 0], 'b-', linewidth=2, label='Jóvenes (0-14)')
    ax2.plot(años_mexico, y_mexico[:, 1], 'g-', linewidth=2, label='Adultos (15-64)')
    ax2.plot(años_mexico, y_mexico[:, 2], 'r-', linewidth=2, label='Mayores (65+)')
    ax2.set_xlabel('Año', fontsize=12)
    ax2.set_ylabel('Población', fontsize=12)
    ax2.yaxis.set_major_formatter(formatter)
    ax2.set_title('MÉXICO: Proyección Demográfica', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    # Gráfica 3: Población Total
    ax3 = axes[1, 0]
    pob_total_chile = y_chile.sum(axis=1)
    pob_total_mexico = y_mexico.sum(axis=1)
    ax3.plot(años_chile, pob_total_chile, 'blue', linestyle='-', linewidth=2, label='Chile')
    ax3.plot(años_mexico, pob_total_mexico, 'green', linestyle='--', linewidth=2, label='México')
    ax3.set_xlabel('Año', fontsize=12)
    ax3.set_ylabel('Población Total', fontsize=12) 
    ax3.yaxis.set_major_formatter(formatter)
    ax3.set_title('Comparación: Población Total', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)

    # Gráfica 4: Índice de Dependencia
    ax4 = axes[1, 1]
    with np.errstate(divide='ignore', invalid='ignore'):
        indice_dep_chile = (y_chile[:, 0] + y_chile[:, 2]) / y_chile[:, 1]
        indice_dep_mexico = (y_mexico[:, 0] + y_mexico[:, 2]) / y_mexico[:, 1]
    
    ax4.plot(años_chile, indice_dep_chile, 'blue', linestyle='-', linewidth=2, label='Chile')
    ax4.plot(años_mexico, indice_dep_mexico, 'green', linestyle='--', linewidth=2, label='México')
    ax4.set_xlabel('Año', fontsize=12)
    ax4.set_ylabel('Índice (Dependientes / Activos)', fontsize=12)
    ax4.set_title('Índice de Dependencia Demográfica', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    
    plt.show()