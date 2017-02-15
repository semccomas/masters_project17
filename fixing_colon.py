import pandas as pd
data = pd.read_csv('~/Downloads/colonALL.csv', index_col = 0) 
conc = data.loc[:, [col for col in data.columns if 'oncentration ' in col]] * 10**9
print conc
conc.to_csv('~/Downloads/colonALL_mol-g.csv')

