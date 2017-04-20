import numpy as np

cguess_flat = np.random.rand((14))
a = np.zeros((3, np.shape(cguess_flat)[0]))
sample = 3 
CL_shape = [2, 3]
P_shape = [4, 2]
len_CL_flat = 6
len_P_flat = 8
cell_number = 2

c = 0
for y in xrange(cell_number * sample):
	a[(c), ((len(cguess_flat) - 1) - y)] = 1   #just python indexing issues, in matlab that should actually just be the len
	if y != 0 and y % cell_number == 1:
		c = c + 1


'''
a = np.zeros((np.shape(cguess_flat)[0], 3))
cguess_flat = np.random.rand((14))
therefore:
X X X X X X X X X X X X X X 
sample = 3
CL_shape = [2, 3]   
therefore: 
X X X
X X X

P_shape = [4, 2]
therefore: 
X X
X X
X X
X X

len_P_flat = 8
len_CL_flat = 6

remember that matlab and python have different indexing but their shapes are the same 


something like:

for x in xrange(sample):
	for y in xrange(??):
		c = c + 1

cell_number * sample = 6
14 - 1 and 14 - 2
14 - 3 and 14 - 4
14 - 5 and 14 - 6


Goal:
. . . . . . . . . . . . 1 1
. . . . . . . . . . 1 1 . .
. . . . . . . . 1 1 . . . .


or

. . . . . . . . 1 1 . . . .
. . . . . . . . . . 1 1 . .
. . . . . . . . . . . . 1 1

dots are zeros its just easier to see the ones
'''