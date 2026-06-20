#!/usr/bin/env python

""" 

Generates a Smooth Gradient of Inflation/Interest Rates over a given range of percentages (Interest rate parameters input in percentages)

Calculates their decay with a given (Time) parameter and generates a Grid, Each column representing the time decay of a given parameter (Cash), with each row going further into the Decay i.e. Further into the Time Axis.

VGrid(Cash, Time, StartRate, EndRate, SepRate)

    Cash - Cash amount to calculate inflation for
    Time - Amount of Time Periods
    
    TAKEN AS PERCENTAGE IN DECIMAL - 1% = 1, 10% = 10
    ---------------------
    StartRate - The Starting column of Interest Rates
    EndRate - The ending column of Interest Rates
    SepRate - The seperation between generated rates


"""

import numpy as np
import matplotlib.pyplot as plt

def Vdecay(Rate, Time, Cashflow): #Function for discounting Cash to present value for the flow of Time due to inflation rates
    return Cashflow / ((1 + Rate)**Time)

def RateFunc(StartRate, EndRate, SepRate): #Sets up interest rate matrix
    Rate = np.arange(StartRate/100, EndRate/100, SepRate/100) #I wanna use arange for the rates because i want to make a step/gradient for the rates

    return Rate
    
def TimeFunc(Time): #Sets up time matrix
    Time = np.arange(0, Time, 1) 
    return Time    

#might aswell use it for Time too

#I wanna be able to create a grid, and have it compute Vdecay for each element with corresponding rate and time, i want it to be functional for all times and rates
#Last time it was forced to be Square limiting usability

#Should remove np.tile if we are doing it element wise 

def VGrid(Cash, Time, StartRate, EndRate, SepRate):

    Rate = RateFunc(StartRate, EndRate, SepRate)
    Time = TimeFunc(Time)

    Timek, Ratek = np.meshgrid(Time, Rate, indexing="ij")
    
    VGrid = Vdecay(Ratek, Timek, Cash)

    Imaging = plt.contourf(Timek, Ratek, VGrid)
    plt.colorbar()
    plt.show()
    
    return VGrid

VGrid(1000, 50, 0, 5, 0.1)

print(VGrid)


if  __name__ == "__main__":
    print()    

