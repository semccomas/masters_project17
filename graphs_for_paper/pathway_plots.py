#### data from 24/2. If you change something (i.e. normalization, etc...) then DONT FORGET TO CHANGE THIS!!!!!!!!!!!!!!!!! The normalization used right now includes
### PARK7 and does imputation from the normal distribution, not with -15 or 0 or whatever


import pandas as pd 
data = pd.read_csv('~/Desktop/Masters_Thesis/data/all_data_processed_park7_norm_with_annotations.csv', index_col = -2)

a = data.loc[:,'C: GOMF name'].dropna().tolist()

for line in a:
	line = line.split('\n')
	for l in line:
		l = l.split(';')
		try:
			print l[1]
		except IndexError:
			pass	