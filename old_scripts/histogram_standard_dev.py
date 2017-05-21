import pandas as pd 
import numpy as np 

while True:
	input_file = raw_input('Use data with original colon concentration or adjusted?  ')
	if input_file.lower() not in ('original', 'adjusted'):
		print 'write "original" or "adjusted"'
		continue
	if input_file.lower() == 'original':
		data = pd.read_csv('~/Desktop/Masters_Thesis/data/transformed_all_data_before_changed_colon_conc.csv', index_col = 0)
		print 
		print 'using original matrix'
		break
	if input_file.lower() == 'adjusted':		
		data = pd.read_csv('~/Desktop/Masters_Thesis/data/transformed_all_data.csv', index_col = 0)
		print
		print 'using adjusted matrix'
		break




print 'standard deviation of histograms: ', data.std().std()   #the standard deviation of the histograms
print 'average value in histograms: ' , data.mean().mean()


jej = data.loc[:, [col for col in data if 'Jejunum' in col]]#.mean()
co = data.loc[:, [col for col in data if 'Colon' in col]]#.mean()
cac = data.loc[:, [col for col in data if 'Caco' in col]]#.mean()

jej = jej.mean().mean()
co = co.mean().mean()
cac = cac.mean().mean()

compare = [jej, co, cac]
print 'standard deviation between the 3 sample types', np.std(compare)