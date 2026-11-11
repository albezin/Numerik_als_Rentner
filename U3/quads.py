import numpy as np

def bit_reverse(N):
    sigma = np.zeros(2**N, dtype=int)
    for k in range(N):
        for j in range(2**k):
            sigma[j + 2**k] = sigma[j] + 2**(N - k - 1)
    return sigma

def integrate(f,a,b,xq = [0,1],wq = [0.5,0.5],n = 1):
    s = 0
    for i in range (n):
        an = ((b-a)/n)*i + a
        for j in range(len(xq)):
            s = s + ((b-a)/n)*wq[j]*f(an+((b-a)/n)*xq[j])

def fft(y):
    y = np.array(y, dtype=complex)
    m = len(y)
    n = np.log2(m)
    y = y[bit_reverse(n)]
    for i in range(1,n-1):
        mi = 2**m
        w = np.exp(-2*np.pi*1j/mi)
        for j in range(0,m,mi):
            for l in range(mi/2):
                u = y[j+1]
                v = (w**l)*y[j+l+mi/2]
                y[j+l] = u+v
                y[j+l + m//2] = u-v

    return y

#anstatt exp(-2ipi/mi) holt man 2ipi/mi also muss man mit 1/N ausgleichen,
#so muss ich meine ifft funktion einmal ein vorzeichen ändern und am ende 1/n rechnen das wars

if __name__ == '__main__':
    s = integrate(np.sin,0,np.pi, n = 500)
    print(s)
