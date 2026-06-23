#!/usr/bin/env python

""" 




"""
import numpy as np
import matplotlib.pyplot as plt

def PV(Rate, Time, FutureCash):
    return FutureCash / ((1 + Rate)**Time)


# Costs = Function(cash)
# Benefits = Function(FutureCash)

Benefits = 100
Costs = 10
Time = 0
Rate = 0.02


# NPV = PV(Benefits) - PV(Costs)
Var = PV(Rate, Time, Benefits) - PV(Rate, Time, Costs)

print(Var)




if __name__ == "__main__":
    print()