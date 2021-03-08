import pandas as pd

df = pd.read_csv('Salaries.csv')

df.ndim

df.shape

df.columns

df.head()

df.tail()

df.sample()

df.sample()

df.sample()

df['rank'].unique()
df['sex'].unique()



df['rank'].value_counts()
df['sex'].value_counts()

df[['rank', 'salary']]

df['salary'] > 120000

df1 = df[df['salary'] > 120000]
