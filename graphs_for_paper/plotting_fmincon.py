import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

o = open('./diaryfminconbackup.txt').read().splitlines()
output1 = [ ] 
for line in o:
	line = line.split()
	if len(line) == 6:
		output1.append(line)

output = [ ]
for n, line in enumerate(output1):
	if n == 0 or line[0] != 'Iter':
		output.append(line)


output = np.asarray(output)
output = pd.DataFrame(output[1:,1:], index = output[1:,0], columns = output[0,1:])

i = list(output.index)
fx = output.loc[:,'f(x)']
step = output.loc[:, 'step']
feval = output.loc[:, 'F-count']

print output

fig, (ax2, ax1) = plt.subplots(2, sharex = True)
ax1.scatter(i, step, color = '#000000', label = 'Step')
ax2.scatter(i, fx, color = '#FF8C73', label = 'F(x)')

ax1.set_ylabel('Step size', labelpad = 10)
ax2.set_ylabel('F(x)')
ax1.set_xlabel(' ')
ax1.set_xlabel('Iterations')
plt.savefig('MATLAB_eval.png', dpi = 1000)

#fval = Objective function value at the solution, returned as a real number. Generally, fval = fun(x).
'''
Idea for surface plot.... save sum of P and sum of CL each time. (could do that in objective funct), and then you have this 3d surface of sum(P), sum(CL) and f(x)

'''

