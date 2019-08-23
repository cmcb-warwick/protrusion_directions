import pandas as pd

df = pd.read_csv('greenchannel_outlines.txt', sep='\t', names=['X','Y','ZT', 'int'])
#print(df)
df['T'] = df['ZT']//118
df['Z'] = df['ZT']%118
df.to_csv('outlines_4d.csv')


#print(df)