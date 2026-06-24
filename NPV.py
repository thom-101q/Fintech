#!/usr/bin/env python

""" 
This script calculates the net present value of a financial deal using numpy.

# The goal is to make a interperatable function with easily adjusted parameters.




"""
import numpy as np
import matplotlib.pyplot as plt

def PV(Rate, Time, FutureCash):
    
    return (FutureCash / ((1 + Rate)**Time))

# Costs = Function(cash)
# Benefits = Function(FutureCash)
def Benefits(B_Cashflow, B_Rate):
    # any function Benefits
    # develop way to imput the benefit of any project
    # I'm gonna start with basic stream of compounding cash flows
    
    return B_Cashflow * (1 + B_Rate)**Time

def Costs(Cost, Year):
    #Want a cost function just like benefits
    #For now we're gonna say its a fixed x year cost of x cash each#
    empty = np.zeros(10 - Year)
    Cost = Cost * np.linspace(1, 1, Year)
    Cost = np.append(Cost, empty)
    
    return Cost



Costs = Costs(5000, 3)
Time = np.arange(0, 10, 1)

Rate = 0.02

Benefits = Benefits(1000, 0.08)

#np.meshgrid does not work for three variables
# K_Time, K_Costs = np.meshgrid(Time, Costs, indexing="ij")


# This needs to go inside the final function for NPV
for x in range(np.size(Time)):
    Benefits[x] = PV(0.02, Time[x], Benefits[x])
    Costs[x] = PV(0.02, Time[x], Costs[x])
    print(Benefits[x])

def NPV():

    NPV = np.sum(Benefts) - np.sum(Costs)

# # NPV = PV(Benefits) - PV(Costs)
# Var = PV(Rate, Time, Benefits) - PV(Rate, Time, Costs)

# print(Var)




if __name__ == "__main__":
    print()