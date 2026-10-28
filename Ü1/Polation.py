import numpy as np
import matplotlib.pyplot as plt
from hansi import dividierte_differenzen

def f(x):
    return pow(1+10*pow(x,2),-1)

def newton(x, x_stutz,koeffs):
    n = len(x_stutz)
    poly = 0
    for k in range(n):
        K = 1
        for i in range(k):
            K =  K * (x-x_stutz[i])
        poly = poly + koeffs[k] * K
    return poly

gitter = np.linspace(-1,1,201)
x_stutz = np.linspace(-1,1,11)
n = len(x_stutz)

koeffs = dividierte_differenzen(x_stutz,f(x_stutz))



y = f(gitter)
p = newton(gitter, x_stutz, koeffs)

plt.plot(gitter, y, label="f(x)")
plt.plot(gitter, p, "--", label="Newton")
plt.plot(x_stutz, f(x_stutz), "o", label="Stütz")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton Horner")
plt.legend()
plt.grid(True)
plt.legend()
plt.show()



