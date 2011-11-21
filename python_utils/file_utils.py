""" This module extracts a line with a key word
"""

###############################################################################

def get_line(datafile,keyword,col):

#	open file
	filein = open(datafile)
	lines = filein.read().splitlines()

#	create list
	varlist = []

# 	begin looping
	i = 0
	while i < len(lines):

#		check to see if line has info
		if len(lines[i].split()) < 1:
			i += 1
			continue

#		split line
		sline = lines[i].split()

#		look for keyword
		if lines[i].find(keyword) == -1: 
			i += 1
			continue

#		keyword found bank col
		varlist.append(float(sline[col]))

#		increment line
		i += 1

#	return list
	return varlist
