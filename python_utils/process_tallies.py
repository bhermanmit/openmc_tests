#! /usr/bin/python

# set imports
from uncertainties import ufloat
from uncertainties import unumpy
from file_utils import get_line
from sys import argv

# get inputs
k_eff = ufloat((argv[1],argv[2]))
filename = argv[3]

# get total reaction rate from file
total_m = get_line(filename,'Total',3)
total_u = get_line(filename,'Total',5)

# get scattering reaction rate from file
scatt_m = get_line(filename,'Scattering Production',3)
scatt_u = get_line(filename,'Scattering Production',5)

# get nu-fission reaction rate from file
nfiss_m = get_line(filename,'Nu-Fission',2)
nfiss_u = get_line(filename,'Nu-Fission',4)

# get outgoing left
curr_out_l_m = get_line(filename,'Outgoing Current to Left',4)
curr_out_l_u = get_line(filename,'Outgoing Current to Left',6)

# get incoming left
curr_inc_l_m = get_line(filename,'Incoming Current from Left',4)
curr_inc_l_u = get_line(filename,'Incoming Current from Left',6)

# get incoming right 
curr_inc_r_m = get_line(filename,'Incoming Current from Right',4)
curr_inc_r_u = get_line(filename,'Incoming Current from Right',6)

# get outgoing left
curr_out_r_m = get_line(filename,'Outgoing Current to Right',4)
curr_out_r_u = get_line(filename,'Outgoing Current to Right',6)

# place all in numpy ufloat array
total = unumpy.uarray((total_m,total_u))
scatt = unumpy.uarray((scatt_m,scatt_u))
nfiss = unumpy.uarray((nfiss_m,nfiss_u))
curr_out_l = unumpy.uarray((curr_out_l_m,curr_out_l_u))
curr_inc_l = unumpy.uarray((curr_inc_l_m,curr_inc_l_u))
curr_inc_r = unumpy.uarray((curr_inc_r_m,curr_inc_r_u))
curr_out_r = unumpy.uarray((curr_out_r_m,curr_out_r_u))

# calculate net current
curr_l = curr_inc_l - curr_out_l
curr_r = curr_out_r - curr_inc_r

# calculate keff
k_eff_cell = nfiss/( (curr_r - curr_l) + total - scatt )

print k_eff_cell

# calculate denominator
den = (curr_r - curr_l) + total - scatt
print den

# print curr_l
# print curr_r

# print total
# print scatt
# print nfiss
# print curr_out_l
# print curr_inc_l
# print curr_inc_r
# print curr_out_r

# print total_m
# print total_u
# print scatt_m
# print scatt_u
# print nfiss_m
# print nfiss_u
# print curr_out_l_m
# print curr_out_l_u
# print curr_inc_l_m
# print curr_inc_l_u
# print curr_inc_r_m
# print curr_inc_r_u
# print curr_out_r_m
# print curr_out_r_u
