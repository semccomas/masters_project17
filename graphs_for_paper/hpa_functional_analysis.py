import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  


HPA = pd.read_csv('~/Desktop/Masters_Thesis/data/normal_tissue.csv', index_col = 1)
data = pd.read_csv('~/Desktop/Masters_Thesis/data/for_plotting_project/pca_loadings_protein_after_data_procc.csv', decimal = ',', index_col = -1)



comp1 = data.loc[:,['Component 1']]
comp2 = data.loc[:, ['Component 2']]

def process (df):
	df = df.apply(lambda x: x.str.replace(",",".")).astype(float)
	below = df[comp1[comp1[:] > 0]]
	return below
