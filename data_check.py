import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sys

# data in and data out
data = pd.read_csv('~/Desktop/Masters_Thesis/data/jejunum_csv.csv', index_col = 0, header = 0)
data = data.dropna()    #remove NaN's, yes it actualy removes them instead of replacing with 0 yes I checked
csv_out = '~/Desktop/Masters_Thesis/data/jejunum_cutoff.csv'


# get pep and peptides df's
pep = data.loc[:,'PEP'].tolist()
peptides = data.loc[:, [col for col in data.columns if 'Peptides ' in col]] #it does count that space in there so it's only the individual peptides for each sample




# info on peptides and pep when you have the certain cutoff number
def find_peptide_percent (column, number, list_name):
	list_peptides = peptides.iloc[:, column].tolist()
	list_pep = [ ] 
	count = 0
	for pep_val, val in zip(pep, list_peptides):     #loop through both so that you can find the pep's of the ones that are above the 'threshold'. They are from the same df so they will always be zip-able
		if val <= number:
			count = count + 1
		else:
			list_pep.append(pep_val)

	print str(count), 'proteins in {0} with <= {1} peptides' .format(list_name, str(number))
	print str(count/float(len(list_peptides)) * 100), '%', 'percentage of total proteins in {0}' .format(list_name)
	print np.mean(pep), 'mean PEP......', np.mean(list_pep), 'would be mean PEP after removing low peptide matches'     #not perfect but a mean PEP is kind of the avg FDR then
	print 




#defining cutoff by user
while True:
	cutoff = raw_input('Cutoff peptide number? ')
	try:
		cutoff = int(cutoff)
	except ValueError:
		print "must be an integer!     "
		continue
	if cutoff < 0:
		print "must be positive!     "
		continue
	else:
		print 'cutoff = ', cutoff 
		break



for x in xrange(0, 10):
	find_peptide_percent(x, cutoff, (str(peptides.columns[x])))   #using less than or equal to, so the number here will be included 






#filtering prompt
while True:
	var = raw_input("Filter out these low peptide count proteins?? ")
	if var.lower() not in ('yes', 'no'):
		print '{0} is not valid response, yes or no' .format(var)
		continue 
	elif var.lower() == 'no':
		print 'finished'
		break
	elif var.lower() == 'yes':
		filtered = data[peptides.mean(axis = 1) > cutoff]     #if the mean of the whole row of peptides is greater than two, then keep it and use the OG matrix, data
		filtered.to_csv(csv_out)
		print 'writing new csv dataframe to file: {0}' .format(csv_out)
		break




