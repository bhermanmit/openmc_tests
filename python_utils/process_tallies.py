#!/usr/bin/env python

from file_utils import get_udata
from sys import argv

# get inputs
filename = argv[1]

# get total reaction rate from file
total = get_udata(filename,'Total')

# get scattering reaction rate from file
scatt = get_udata(filename,'Scattering Production')

# get nu-fission reaction rate from file
nfiss = get_udata(filename,'Nu-Fission')

# get currents on left face
curr_out_l = get_udata(filename,'Outgoing Current to Left')
curr_inc_l = get_udata(filename,'Incoming Current from Left')

# get currents on right face
curr_inc_r = get_udata(filename,'Incoming Current from Right')
curr_out_r = get_udata(filename,'Outgoing Current to Right')

# calculate net current
curr_l = curr_out_l - curr_inc_l
curr_r = curr_out_r - curr_inc_r
current = curr_l + curr_r

# calculate denominator
denominator = current + total - scatt

# calculate keff
k_eff = nfiss/denominator

n_cells = len(k_eff)
for i in range(n_cells):
    print "Cell " + str(i)
    print "  Nu fission  = " + str(nfiss[i])
    print "  Net current = " + str(current[i])
    print "  Total       = " + str(total[i])
    print "  Nu scatter  = " + str(scatt[i])
    print "  Denominator = " + str(denominator[i])
    print "  keff        = " + str(k_eff[i])
