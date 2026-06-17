#!/usr/bin/env python

""" 

Rewriting and testing PV.py with better numpy functionality

Creates a numpy array given a set of rates (Percentages) and calculates the time decay for each rate, creating a square matrix

Probem: the matrix is forced to be square meaning number of times = number of rates


"""

import numpy as np

def Vdecay(Rate, Time, Cashflow): #Function for discounting Cash to present value for the flow of Time due to inflation rates
    return Cashflow / ((1 + Rate)**Time)

def RateFunc(Start, End, Sep): #Sets up interest rate matrix
    Rate = np.arange(Start/100, End/100, Sep/100) #I wanna use arange for the rates because i want to make a step/gradient for the rates

    return Rate
    
def TimeFunc(Time): #Sets up time matrix
    Time = np.arange(0, Time, 1) 
    return Time    

#might aswell use it for Time too

#I wanna be able to create a grid, and have it compute Vdecay for each element with corresponding rate and time, i want it to be functional for all times and rates
#Last time it was forced to be Square limiting usability

#Should remove np.tile if we are doing it element wise 
Rate = RateFunc(0, 4, 1)
Time = TimeFunc(50)

Timek, Ratek = np.meshgrid(Time, Rate, indexing="ij")

VdecayGrid = Vdecay(Ratek, Timek, 1000)

print(VdecayGrid)


if  __name__ == "__main__":
    print()    

