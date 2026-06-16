#!/usr/bin/env python

""" 

Rewriting and testing PV.py with better numpy functionality

Creates a numpy array given a set of rates (Percentages) and calculates the time decay for each rate, creating a square matrix

Probem: the matrix is forced to be square meaning number of times = number of rates


"""

import numpy as np

def Vdecay(Rate, Time, Cashflow): #Function for discounting Cash to present value for the flow of Time due to inflation rates
    return Cashflow / ((1 + Rate)**Time)

def Rate(Start, End, Sep): #Sets up interest rate matrix
    Rate = np.arange(Start, End, Sep) #I wanna use arange for the rates because i want to make a step/gradient for the rates

    return Rate
    
def Time(Time): #Sets up time matrix
    Time = np.arange(0, Time, 1) #might aswell use it for TIme too

#I wanna be able to create a grid, and have it compute Vdecay for each element with corresponding rate and time, i want it to be functional for all times and rates
#Last time it was forced to be Square limiting usability

#Should remove np.tile if we are doing it element wise CashGrid[i][j]

Ratek, Timek = np.meshgrid(Rate, Time, indexing="ij")
for i in range(nx):
    for j in range(ny):
        #Treats xv[i, j], yv[i, j]
        Cashgrid[] = Vdecay(Rate[], Time[], Cashflow)



    # CashGrid = np.ones((I_size, T_size)) * Cashflow
    
    # for i in x:
    #     for j in y:
    #         CashGrid[i][j] = PV_equation(I[i][j], T[i][j], Cashflow)
        

print(Cashgrid)




