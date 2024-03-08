# Lekcja 14, 04.01.2024 

# Nowy projekt: Dziennik ocen (przedmioty, oceny, wagi)   


# Pandas

import pandas as pd
import matplotlib.pyplot as plt


dane = {
    'Name': ['Anna', 'Bob', 'Charles', 'Diana', 'Eric'],
    'Age': [23, 34, 45, 29, 31],
    'City': ['London', 'New York', 'New York', 'Paris', 'New York'],
    "Weight" : [90, 70, 80, 65, 68]
}

df = pd.DataFrame(dane)
# print(df)
# print(df.head(2))
# df.info()
# print(df.tail(2))

new_df = df.dropna() # usuwa wiersze, gdzie pojawia się wartość None lub NaN

# df.plot()
# plt.show()




# Treść: Mając poniższy DataFrame df, wybierz wszystkie wiersze, gdzie wartość w kolumnie 'Age' jest większa niż 32 i wartość w kolumnie 'City' to 'New York'.

df1 = df[(df["Age"] > 32) & (df["City"] == "New York")]
# print(df1)

df2 = df[(df["City"] == "Paris") | (df["City"] == "London")]
# print(df2)

# Pogrupuj dane wg wieku:
df3 = df.groupby("City")["Age"].mean()
print(df3)

data1 = {
    'Employee': ['Susan', 'Tom', 'Anna', 'John', 'Andrew'],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Salary': [50000, 60000, 70000, 55000, 48000]
}

data2 = {
        'Employee': ['Susan', 'Tom', 'Anna', 'John', 'Andrew'],
        'Hire_Date': ['2019-01-23', '2020-02-10', '2018-11-15', '2020-03-10', '2018-10-15']
}
df_3 = pd.DataFrame(data2)
print(df_3)

df_2 = pd.DataFrame(data1)
# print(df_2)

df4 = df_2.groupby("Department")["Salary"].mean()
print(df4)

# połącz dwie ramki danych
df_merged = pd.merge(df_2, df_3, on="Employee")
print(df_merged)