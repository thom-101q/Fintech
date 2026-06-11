import numpy as np
import matplotlib.pyplot as plt


Cashflow = 1000
I = [0.01, 0.05, 0.10]
I_0 = 0.01


T = [1, 2, 3]
T_0 = 0

print(np.size(T))
#np.vstack(array1, array2) to stack array

PV_I = []
PV_T = []
PV = []

CashGrid = np.ones((3, 3)) * Cashflow
#print(CashGrid)
#for x in I:
#    PV_I = np.append(PV_I, Cashflow*(1 - x) ** T_0)
#    PV_T = np.append(PV_T, Cashflow*(1 - I_0) ** x)

for x in I:
    PV_I = np.append(PV_I, Cashflow*(1 - x) ** T_0)
for x in T:
    PV_T = np.append(PV_T, Cashflow*(1 - I_0) ** x)

PV_T = np.vstack(PV_T)

#print(PV_I)
# #print(PV_T)

# CashGrid_T = np.empty((3,1))
# print(np.empty((3,1)))
I_0 = 0.01
#for T in T:
    #CashGrid = CashGrid[:,0:T]*(1-I_0) ** T
    #CashGrid_T = np.c_[CashGrid_T, CashGrid]
# T = [1, 2, 3]
# for T in [1, 2, 3]:
#     CashGrid = (lambda x: x-T)(CashGrid[:,0:T])
#     CashGrid_T = np.c_[CashGrid_T, CashGrid]
#     print(CashGrid_T)
# print(CashGrid_T)
    

#print(CashGrid)

# for x in T: 
#     CashGrid[x] = Cashflow*(1 - I_0) ** x
#     print(CashGrid)

def PV(I, T, Cashflow):
    return Cashflow * ((1- I)**T)
    

for I, T in zip(I, T):
    #CashGrid[:,:T] = CashGrid[:,:T]*(1 - I) ** T
    Newcash = PV(I, T, CashGrid[:, T-1:T])
    CashGrid[:, T-1:T] = Newcash
    Newcash = PV(I, T, CashGrid[T-1:T, :])
    CashGrid[T-1:T, :] = Newcash
    print(CashGrid)





if __name__ == "__main__":
    print("Executed")



