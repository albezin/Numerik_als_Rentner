import numpy as np

def dividierte_differenzen(x_stuetz, y_stuetz):
    assert len(x_stuetz) == len(y_stuetz), "Die Stützstellen liegen nicht als Tupel vor."
    result = y_stuetz.copy()
    
    for m in range(1, len(x_stuetz)):
        for i in range(len(x_stuetz)-1, m-1, -1):
            result[i] = (result[i] - result[i-1]) / (x_stuetz[i] - x_stuetz[i-m])

    return result

def dividierte_differenzen_horner(x_stuetz, y_stuetz, x_eval):
    assert len(x_stuetz) == len(y_stuetz), "Die Stützstellen liegen nicht als Tupel vor."

    # Calculate coefficients of Newton's divided difference representation
    coeff  = dividierte_differenzen(x_stuetz, y_stuetz)
    result = coeff[-1] * np.ones_like(x_eval) # Initialize return value

    # Iteratively evaluate using Horner's method
    for i in range(len(x_stuetz) - 2, -1, -1):
        result = result * (x_eval - x_stuetz[i]) + coeff[i]

    return result

def bit_reverse(N):
    sigma = np.zeros(2**N, dtype=int)
    for k in range(N):
        for j in range(2**k):
            sigma[j + 2**k] = sigma[j] + 2**(N - k - 1)
    return sigma

def getxstuetz(n):
    tscheb = lambda a, b, n: .5 * ((b-a) * np.cos((2*np.arange(n,-1,-1)+1)*np.pi / (2*n+2)) +a+b)

    # Generate Chebyshev nodes and sort in ascending order
    x1 = np.sort(tscheb(0, 1, n))  # Chebyshev nodes sorted in ascending order

    # Reorder nodes with alternating smallest and largest elements
    tmp, x2 = list(x1), []

    while len(tmp) > 1:
        vmax, vmin = max(tmp), min(tmp)
        imax, imin = tmp.index(vmax), tmp.index(vmin)
        
        # Remove the largest and smallest elements
        tmp.pop(imax)
        tmp.pop(imin if imin < imax else imin - 1)
        
        # Append smallest and largest to x2
        x2.extend([vmin, vmax])

    # Append the remaining element (if any)
    x2.extend(tmp)
    
    return np.array(x1), np.array(x2)
    