import numpy as np


def dividierte_differenzen(x_stuetz, y_stuetz):
    x = np.array(x_stuetz, dtype=np.float64)
    p = np.array(y_stuetz, dtype=np.float64)
    n = len(x)

    for k in range(1, n):
        p[k:n] = (p[k:n] - p[k - 1:n - 1]) / (x[k:n] - x[0:n - k])
    return p


if __name__ == '__main__':

    def f(x):
        return 1.0 / (1.0 + 10.0 * x ** 2)

    x_aequi_stuetz = np.arange(-1.0, 1.0 + 1e-9, 0.2)
    y_aequi_stuetz = f(x_aequi_stuetz)

    # Tschebyscheff-Knoten
    n = 10
    i = np.arange(n + 1)
    x_tschebychef = np.cos((2 * i + 1) * np.pi / (2 * n + 2))

    x_tschebychef = np.sort(x_tschebychef)
    y_tschebychef = f(x_tschebychef)

    koeffs_aequi = dividierte_differenzen(x_aequi_stuetz, y_aequi_stuetz)
    koeffs_tschebychef = dividierte_differenzen(x_tschebychef, y_tschebychef)


    print("Newton Darstellung :")
    for k, (x_k, p_k) in enumerate(zip(x_aequi_stuetz, koeffs_aequi)):
        print(f"{k:2d}  {x_k: 8.4f}  {p_k: 16.8f}")

    print("\nTschebyscheff-Knoten:")
    for k, (x_k, p_k) in enumerate(zip(x_tschebychef, koeffs_tschebychef)):
        print(f"{k:2d}  {x_k: 8.4f}  {p_k: 16.8f}")