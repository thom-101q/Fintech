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



# def Benefits(B_Cashflow, B_Rate):
#     # any function Benefits
#     # develop way to imput the benefit of any project
#     # I'm gonna start with basic stream of compounding cash flows
    
#     return B_Cashflow * (1 + B_Rate)**Time




def Costs(Cost, Year):
    #Want a cost function just like benefits
    #For now we're gonna say its a fixed x year cost of x cash each#
    empty = np.zeros(10 - Year)
    Cost = Cost * np.linspace(1, 1, Year)
    Cost = np.append(Cost, empty)
    
    return Cost





def NPV(Rate, B_Cashflow, B_Rate):

    ArrCosts = Costs(5000, 3)
    Time = np.arange(0, 10, 1)
    Benefits = B_Cashflow * (1 + (B_Rate/100))**Time
    
    # This needs to go inside the final function for NPV
    for x in range(np.size(Time)):
        Benefits[x] = PV(Rate/100, Time[x], Benefits[x])
        ArrCosts[x] = PV(Rate/100, Time[x], ArrCosts[x])
        # print(Benefits[x])
        # print(np.sum(ArrCosts))
    NPV = np.sum(Benefits) - np.sum(ArrCosts)
    return NPV

# # NPV = PV(Benefits) - PV(Costs)
# Var = PV(Rate, Time, Benefits) - PV(Rate, Time, Costs)

# print(Var)

# NPV(2, 1000, 8)
# print(NPV)

if __name__ == "__main__":
    print()