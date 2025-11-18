import numpy as np


def RK4(func, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    n = len(t_values)
    y_values = np.zeros((n, len(y0)), dtype=float)
    y_values[0] = y0

    for i in range(1, n):
        k1 = np.array(func(t_values[i - 1], y_values[i - 1]))
        k2 = np.array(func(t_values[i - 1] + h / 2, y_values[i - 1] + h * k1 / 2))
        k3 = np.array(func(t_values[i - 1] + h / 2, y_values[i - 1] + h * k2 / 2))
        k4 = np.array(func(t_values[i - 1] + h, y_values[i - 1] + h * k3))
        y_values[i] = y_values[i - 1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_values, y_values
