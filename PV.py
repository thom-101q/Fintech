import numpy as np
import matplotlib.pyplot as plt


Cashflow = 1000
I = [0.01, 0.05, 0.10]
T = [1, 2, 3]

for x in range(1):
    I = np.vstack((I, I, I))
    T = np.vstack((T, T, T))




CashGrid = np.ones((3, 3)) * Cashflow

def PV(I, T, Cashflow): #from Itertools
    return Cashflow * ((1- I)**T)

def product(*iterables, repeat=1):
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111

    if repeat < 0:
        raise ValueError('repeat argument cannot be negative')
    pools = [tuple(pool) for pool in iterables] * repeat

    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)

# for I, T in zip(I, T):
#     #CashGrid[:,:T] = CashGrid[:,:T]*(1 - I) ** T
#     #CashGrid[:, :] = 


    
#     Newcash = PV(I, T, CashGrid[:, T-1:T])
#     CashGrid[:, T-1:T] = Newcash
#     Newcash = PV(I, T, CashGrid[T-1:T, :])
#     CashGrid[T-1:T, :] = Newcash
#     print(CashGrid)

#print(CashGrid[0, 0])
#print(I[0, 0])
#print(T[0, 0])
x = 3

y = x

for x, y in product(range(x), range(y)):
    CashGrid[x, y] = PV(I[x, y], T[x, y], Cashflow)
    print(CashGrid[x, y])

print(CashGrid)
# CashGrid[0, 0] = PV(I[0, 0], T[0, 0], CashGrid[0, 0])

#print(CashGrid)

if __name__ == "__main__":
    print("Executed")



