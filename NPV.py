#!/usr/bin/env python

""" 
This script calculates the net present value of a financial deal using numpy.

# The goal is to make a interperatable function with easily adjusted parameters.




"""
import numpy as np
import matplotlib.pyplot as plt
7
def PV(Rate, Time, FutureCash):
    return FutureCash / ((1 + Rate)**Time)


# Costs = Function(cash)
# Benefits = Function(FutureCash)
def Benefits(B_Cashflow, B_Rate):
    # any function Benefits
    # develop way to imput the benefit of any project
    # I'm gonna start with basic stream of compounding cash flows
    
    return B_Cashflow * (1 + B_Rate)**Time

def Costs(Cost):
    #Want a cost function just like benefits
    #For now we're gonna say its a fixed 3 year cost of x cash each#
    empty = np.zeros(10)
    Cost = Cost * np.linspace(1, 1, 3)
    for Cost[0:3] in range(3):
        empty[0:3] = empty[0:3] + Cost[0:3]
        
    return Cost
    

Costs = Costs(5000)
Time = np.arange(0, 10, 1)

Rate = 0.02



Benefits = Benefits(1000, 0.08)

#np.meshgrid does not work for three variables
K_Time, K_Costs = np.meshgrid(Time, Costs, indexing="ij")


# NPV = PV(Benefits) - PV(Costs)
Var = PV(Rate, Time, Benefits) - PV(Rate, Time, Costs)

print(Var)




if __name__ == "__main__":
    print()