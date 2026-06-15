#!/usr/bin/env python

""" 

Rewriting and testing PV.py with better numpy functionality

Creates a numpy array given a set of rates (Percentages) and calculates the time decay for each rate, creating a square matrix

Probem: the matrix is forced to be square meaning number of times = number of rates


"""

import numpy as np

def Vdecay(Rate, Time, Cashflow):
    return Cashflow / ((1 + Interest)**Time)

def Rate(Start, End, Sep)
    Rate = np.arange(Start, End, Sep)

def Time(Time)
    Time = np.arange(0, Time, 1)




