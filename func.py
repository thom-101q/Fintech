import numpy as np
import matplotlib.pyplot as plt


Cashflow = 1000
I = [0.01, 0.02, 0.03]
I_0 = 0.01


T = [1, 2, 3]
T_0 = 1

print(np.size(T))
#np.vstack(array1, array2) to stack array

PV_I = []
PV_T = []
PV = []

CashGrid = np.ones((3, 3)) * Cashflow
print(CashGrid)
#for x in I:
#    PV_I = np.append(PV_I, Cashflow*(1 - x) ** T_0)
#    PV_T = np.append(PV_T, Cashflow*(1 - I_0) ** x)

for x in I:
    PV_I = np.append(PV_I, Cashflow*(1 - x) ** T_0)
for x in T:
    PV_T = np.append(PV_T, Cashflow*(1 - I_0) ** x)

PV_T = np.vstack(PV_T)

#print(PV_I)
#print(PV_T)

CashGrid_T = np.zeros((3,1))
I_0 = 0.01
for T in T:
    CashGrid = CashGrid[:,0:T]*(1-I_0) ** T
    print(CashGrid)
    CashGrid_T = np.c_[CashGrid_T, CashGrid]

print(CashGrid_T)

T_0 = 1



