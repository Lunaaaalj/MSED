import numpy as np
import matplotlib.pyplot as plt

def rk4_sistemaEC(f, a, b, u0, h):
    T = np.arange(a, b + h, h)
    n = len(T)
    m = len(u0)
    U = np.zeros((n, m))
    U[0] = u0

    for j in range(n - 1):
        t = T[j]
        u = U[j]

        k1 = f(t, u)
        k2 = f(t + h/2, u + (h/2)*k1)
        k3 = f(t + h/2, u + (h/2)*k2)
        k4 = f(t + h, u + h*k3)

        U[j+1] = u + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    return U, T


def funcion_demografica(t, z, calcular_natalidad, m_J, m_A, m_E):
    J = z[0]
    A = z[1]
    E = z[2]
    
    b_t = calcular_natalidad(t)
    
    # Tasas de transición (simplificadas)
    transicion_J_a_A = 1/15 
    transicion_A_a_E = 1/50 
    
    dJ_dt = (b_t * A) - (m_J * J) - (transicion_J_a_A * J)
    dA_dt = (transicion_J_a_A * J) - (m_A * A) - (transicion_A_a_E * A)
    dE_dt = (transicion_A_a_E * A) - (m_E * E)
    
    return np.array([dJ_dt, dA_dt, dE_dt])


def funcion_natalidad(b_2025, b_2050, t_inicial=2025, t_final=2050):
    # Pendiente (m)
    m = (b_2050 - b_2025) / (t_final - t_inicial)
    
    # Intercepto (b_val)
    # b = m*t + b_val -> b_val = b - m*t
    b_val = b_2025 - m * t_inicial
    
    def calcular_natalidad(t_real):
        # t_real es el año (ej. 2030)
        return m * t_real + b_val
        
    return calcular_natalidad