import pandas as pd

df = pd.read_csv("Salaries.csv")

df.columns.tolist()

df.dtypes

df['salary']
df.salary

df['rank']
df.rank

df.phd
df.service

filter1 = df['salary'] > 100000

df[filter1].value_counts()

len(df[filter1])


filter2 = (df['salary'] > 100000) & (df['sex'] == 'Female') 

df[filter2]

df.isnull().any(axis = 0)

df.isnull().any(axis = 1)

df[df.isnull().any(axis = 1)]


df = df.dropna()

df.dropna(inplace = True)

df2 = df.fillna(100)


df.iloc[ 5:10 , 0:2 ]

df.iloc[ [5,10] , 0:2 ]


df.iloc[ : , 0:2 ]

df.iloc[10 , :]

