"""
This module extracts a line with a key word
"""

from uncertainties import unumpy

def get_udata(datafile, keyword):

    # create list
    mean = []
    stdev = []

    # begin looping
    for line in open(datafile):
                
        # split line
        words = line.split()

        # check to see if line has info
        if len(words) < 1:
            continue

        # look for keyword
        if line.find(keyword) != -1: 
            # keyword found bank col
            mean.append(float(words[-3]))
            stdev.append(float(words[-1]))

    # return list
    return unumpy.uarray((mean,stdev))
