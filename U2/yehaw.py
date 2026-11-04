
import numpy as np
import matplotlib.pyplot as plt
import Python_Funktionen as pf

def polynomInterpolation(x, y, ord, nu):

    n = len(x) - 1
    anzahl = n // ord

    xe = np.zeros((anzahl, nu))
    ye = np.zeros((anzahl, nu))

    for i in range(anzahl):

        ind = np.arange(i * ord, (i + 1) * ord + 1)

        xe[i, :] = np.linspace(x[ind[0]], x[ind[-1]], nu)

        ye[i, :] = pf.dividierte_differenzen_horner(
            x[ind],
            y[ind],
            xe[i, :]
        )

    xe = xe.reshape(-1)
    ye = ye.reshape(-1)

    return xe, ye

f = lambda x: 1 / (1 + 10*x**2)

x = np.linspace(-1, 1, 7)
y = f(x)

x_plot = np.linspace(-1, 1, 500)
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'k-', label='OF')

for ord in [1, 2, 3]:

    xe, ye = polynomInterpolation(x, y, ord, 100)

    plt.plot(xe, ye, label=f'Grad {ord}')

plt.plot(x, y, 'ro', label='Stützstellen')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Polynominterpolation')
plt.legend()
plt.grid()
plt.show()



