#!/usr/bin/env python


""" DOCSTRING HERE """

import numpy as np
import matplotlib.pyplot as plt


def PV_equation(I, T, Cashflow): #PV Function discounting cash flows
    return Cashflow / ((1 + I)**T)


    
    
    
def PV(Cashflow, Start, End, Sep):
    
    I = np.arange((Start / 100), (End / 100), (Sep / 100))
    I_size = np.size(I)
    I = np.rot90(np.tile(I, (I_size, 1)), k=3)
    
    T = np.arange(1, (I_size+1), 1)
    T_size = np.size(T)
    T = np.tile(T, (T_size, 1))
    
    x = np.arange(0, (I_size), 1)
    y = np.arange(0, (T_size), 1)

    CashGrid = np.ones((I_size, T_size)) * Cashflow
    
    for i in x:
        for j in y:
            CashGrid[i][j] = PV_equation(I[i][j], T[i][j], Cashflow)
            print(CashGrid[i, j])

    print(CashGrid)

PV(1000, 0, 10, 1)

if __name__ == "__main__":
    print("Executed")



