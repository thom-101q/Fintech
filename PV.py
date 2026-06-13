import numpy as np
import matplotlib.pyplot as plt

def PV(I, T, Cashflow): #PV Function discounting cash flows
    return Cashflow / ((1 + I)**T)

Cashflow = 1000
I = [0.01, 0.03, 0.03, 0.05, 0.07]
T = np.arange(1, (np.size(I)+1), 1)
x = np.arange(0, (np.size(I)), 1)
y = x

CashGrid = np.ones((np.size(I), np.size(T))) * Cashflow

I = np.tile(I, (np.size(I), 1))
T = np.tile(T, (np.size(T), 1))

I = np.rot90(I, k=3)

for i in x:
    for j in y:
        CashGrid[i, j] = PV(I[i, j], T[i, j], Cashflow)
        # print(CashGrid[i, j])

print(CashGrid)





if __name__ == "__main__":
    print("Executed")


