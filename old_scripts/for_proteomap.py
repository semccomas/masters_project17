import pandas as pd 
import numpy as np

data = pd.read_csv('~/Desktop/Masters_Thesis/data/data_original_with_all_protein_id.csv')

data = data.rename(columns = {'Protein IDs': 'Protein_IDs_jejH', "Protein IDs.1" : "Protein_IDs_jejJ", "Protein IDs.2": "Protein_IDs_colon", "Protein IDs.3":"Protein_IDs_caco"})


def blah (df, col):
	df = df.dropna()
	col = col.str[0:6]
	return df

jejunumH = data[["Protein_IDs_jejH", "Jejunum concentration (pmol/mg) H10"]].copy()
jejunumJ = data[["Protein_IDs_jejJ", "Concentration (pmol/mg) J2"]].copy()
colon = data[["Protein_IDs_colon", "concentration (mol/g) A1"]].copy()
caco = data[["Protein_IDs_caco", "concentration(pmol/mg)  A3"]].copy()

jejunumH = jejunumH.dropna()
jejunumJ = jejunumJ.dropna()
colon = colon.dropna()
caco = caco.dropna()

jejunumH.Protein_IDs_jejH = jejunumH.Protein_IDs_jejH.str[0:6]

jejunumJ.Protein_IDs_jejJ = jejunumJ.Protein_IDs_jejJ.str[0:6]

colon.Protein_IDs_colon = colon.Protein_IDs_colon.str[0:6]

caco.Protein_IDs_caco = caco.Protein_IDs_caco.str[0:6]

df = jejunumJ # this and the one below you have to change

df = df.drop_duplicates(subset = 'Protein_IDs_jejJ')   # and this too 
np.savetxt('blah.txt', df.values, fmt = '%s', delimiter = '\t')