import pandas as pd 

data = pd.read_csv("~/Desktop/Masters_Thesis/data/protein_ID's.csv", index_col = 0)
data2 = data
data = data.fillna('nana')
data['PROTEIN_ID_ALL'] = data['Protein_IDs_JejunumH'] + ';' + data['Protein_IDs_JejunumF'] + ';' + data['Protein_IDs_Colon'] + ';' + data['Protein_IDs_Caco']

#acidentally named it jejunum F
data.to_csv('testing.csv')






#data['PROTEIN_ID_ALL'] = data['Protein IDs'].map(str) + data['Protein IDs.1']
# this worked the best so far but no delimiter

#data['TEST'] = data[['Protein IDs', 'Protein IDs.1']].apply(lambda x: ';'.join(str(x)), axis = 1)
# this one is funky but also kind of working

#data['PROTEIN_ID_ALL'] = data['Protein IDs'] + ';' + data['Protein IDs.1'] + ';' + data['Protein IDs.2'] + ';' + data['Protein IDs.3']
#kind of working too but also something weird
