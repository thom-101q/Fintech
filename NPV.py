#!/usr/bin/env python

"""

This script calculates the net present value of a financial deal using numpy.
It assumes a stream of cashflows for the Benefits parameters(size, rate, for all time) and a customisable Fixed cost taking parameters(size, time) repeating x amount of years from year 0.

These are two functions represented i want to make it easier to use a greater variety of options for benefits and costs, and not just these hardcoded functions.

Maybe I should look at different financial scenarios in the textbook, and implement them.

"""
import numpy as np
import matplotlib.pyplot as plt

#Maybe a function that defines functions for benefits/cost based on parameters?
# Costs = Function(cash)
# Benefits = Function(FutureCash)

def PV(Rate, Time, FutureCash):
    
    return (FutureCash / ((1 + Rate)**Time))


def NPV(Rate, B_Cashflow, B_Rate, Cost, CostTime, Years):

    #Setting Costs Below, For now we're gonna say its a fixed x year cost of x cash each
    empty = np.zeros(Years)
    ArrCosts = Cost * np.linspace(1, 1, CostTime)
    ArrCosts = np.append(ArrCosts, empty)
    print(ArrCosts)
    
    # set any function to define Benefits
    Time = np.arange(0, (Years+1), 1)
    Benefits = B_Cashflow * (1 + (B_Rate/100))**Time
    # I'm gonna start with basic stream of compounding cash flows
    print(Benefits)
    
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

Result = NPV(2, 1000, 8, 5000, 3, 10)
print(Result)

if __name__ == "__main__":
    print()