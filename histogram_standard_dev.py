import pandas as pd 

data = pd.read_csv('~/Desktop/Masters_Thesis/data/transformed_all_data.csv', index_col = 0)

print data.std().std()   #the standard deviation of the histograms
