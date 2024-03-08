import pandas as pd
import matplotlib as plt

df = pd.read_csv('C:/Users/barte/Desktop/Programiki/male zadania/wybory_sejm_2015.csv')

print(df.head())

df1 = df.groupby('Nr okr.')['Liczba wyborców'].agg("mean", "median", "min", "max")
print(df1.head())

cor = df[['Liczba wyborców', "Otrzymane karty", "Niewykorzystane karty"]].corr()
print(cor)

df2 = df.groupby('Nr okr.')['Liczba wyborców'].sum().plot(kind='bar')
print(df2)

