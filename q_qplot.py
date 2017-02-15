import pandas as pd
import numpy as np
#import pylab
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

## decide if you want to have original or changed files, so don't take them away from Desktop! 
def input_prompt(axis):
	while True:
		table = raw_input('{0} axis, use original or changed data? '.format(axis))
		if table.lower() not in ('original', 'changed'):
			print 'write "original" or "changed"'
			continue
		if table.lower() == 'original':
			data = pd.read_csv('~/Desktop/original_colon_processed.csv', index_col = -1)
			print 'using original matrix {0}' .format(axis)
			break
		if table.lower() == 'changed':
			data = pd.read_csv('~/Desktop/changed_colon_processed.csv', index_col = -1)
			print 'using changed matrix on {0}' .format(axis)
			break
	concentrations = [col for col in data.columns if 'oncentrat' in col]
	c = np.asarray(data.loc[:, concentrations])

	return c, concentrations

### calling function and getting variable names 
x = input_prompt('X')
names_x = x[1]
x = x[0]

y = input_prompt('Y')
names_y = y[1]
y= y[0]

### making plots and comparing r2
while True:
	graph_q = raw_input('Make a q-q graph? ')
	if graph_q.lower() == 'yes':
		for index, name in enumerate(names_x):
			print name, ', index number:', index
		index_x = int(raw_input('Dataset row number for X axis: '))
		index_y = int(raw_input('Dataset row number for Y axis: '))
		x_values = x[:,index_x]
		y_values = y[:,index_y]
		sm.qqplot_2samples(x_values, y_values, xlabel = 'quantiles for ' + names_x[index_x], ylabel = 'quantiles for ' + names_y[index_y],  line = 'r')
		plt.show()
		continue
	else:
		print 'done'
		break

r_values_list = [ ]
for xval in xrange(len(names_x)):
	for yval in xrange(len(names_y)):
		slope, intercept, r_value, p_value, std_err = stats.linregress(x[:,xval], y[:,yval])
		r_values_list.append(r_value)

print min(r_values_list), 'min'
print reduce(lambda x, y: x + y, r_values_list) / len(r_values_list), 'avg'

#stats.probplot(c[:,45], dist="norm", plot=matplotlib)



