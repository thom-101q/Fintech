import numpy as np
import matplotlib.pyplot as plt

def PV_equation(I, T, Cashflow): #PV Function discounting cash flows
    return Cashflow / ((1 + I)**T)

def PV(Cashflow, Start, End, Sep):

    I = np.arange((Start / 100), (End / 100), (Sep / 100))
    # I = [0.01, 0.02, 0.03, 0.04, 0.05]
    T = np.arange(1, (np.size(I)+1), 1)
    x = np.arange(0, (np.size(I)), 1)
    y = x
    
    CashGrid = np.ones((np.size(I), np.size(T))) * Cashflow

    I = np.rot90(np.tile(I, (np.size(I), 1)), k=3) 
    T = np.tile(T, (np.size(T), 1))

    for i in x:
        for j in y:
            CashGrid[i, j] = PV_equation(I[i, j], T[i, j], Cashflow)
            # print(CashGrid[i, j])

    print(CashGrid)



if __name__ == "__main__":
    print("Executed")



