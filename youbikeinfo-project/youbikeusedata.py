#youbike使用效率
import pandas as pd

df = pd.read_csv('youbike.csv')
df = df[['sna','tot', 'sbi', 'bemp']]
print('-'*70)
df['車輛使用率'] = 1-df['sbi']/df['tot']
print(df.head())
print('-'*70)
youbike_used = df[['sna', '車輛使用率']]
print(youbike_used.head())