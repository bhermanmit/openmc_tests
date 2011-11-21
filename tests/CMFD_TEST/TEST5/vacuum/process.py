#! /usr/bin/python

# imports
from uncertainties import ufloat
from uncertainties.umath import *

# Enter data
total = ufloat((8.58862E-2,6.45665E-5))
scatt = ufloat((6.94066E-2,5.89917E-5))
nfiss = ufloat((4.46875E-2,3.36160E-5))

l_i_curr = ufloat((0.180303,2.75471E-3))
l_o_curr = ufloat((0.187978,2.88515E-3))

r_i_curr = ufloat((0.184384,2.82200E-3))
r_o_curr = ufloat((0.184339,2.82283E-3))

k_eff = ufloat((1.76620,2.99895E-4))

# Calculate net currents 
l_curr = l_i_curr - l_o_curr
r_curr = r_o_curr - r_i_curr

# Calculate keff
k_eff_bal = nfiss/(r_curr - l_curr + total - scatt)

# Calculate difference of keff
k_diff = k_eff - k_eff_bal

# print stuff
print k_eff
print k_eff_bal
print k_diff
