import numpy as np
import matplotlib.pyplot as plt



def PV(I, T, Cashflow): #from Itertools
    return Cashflow * ((1- I)**T)

Cashflow = 1000
I = [0.01, 0.03, 0.09]
T = [1, 2, 3]

CashGrid = np.ones((3, 3)) * Cashflow

for x in range(1):
    I = np.vstack((I, I, I))
    T = np.vstack((T, T, T))

I = np.rot90(I, k=3)

x = [0, 1, 2]
y = x

for i in x:
    for j in y:
        CashGrid[i, j] = PV(I[i, j], T[i, j], Cashflow)
        print(CashGrid[i, j])

print(CashGrid)

if __name__ == "__main__":
    print("Executed")



