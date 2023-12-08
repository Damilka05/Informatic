import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = './Mall_Customers.csv'
df = pd.DataFrame()
df = pd.read_csv(file, delimiter=',', index_col=None)


# df_female = df[df['Genre'] == 'Female']
# df_female = df_female.set_index('Genre')
# df_female = df_female.groupby(level="Genre").mean()
# print(df_female['Annual Income (k$)'])


# df = df.set_index(['Genre'])
# df = df.groupby(level="Genre").max()
# print(df)


# df = df[df['Genre'] == 'Male']
# plt.scatter(df['Age'].tolist(), df['Annual Income (k$)'], color = 'red')
# plt.grid()
# plt.xlabel("Male Age")
# plt.ylabel('Annual Income (k$)')
# plt.show()


# df = df[df['Genre'] == 'Male']
# plt.scatter(df['Age'].tolist(), df['Annual Income (k$)'], color = 'red')
# plt.grid()
# plt.xlabel("Male Age")
# plt.ylabel('Annual Income (k$)')
# plt.show()

# df_male = df[df[['Genre'] == 'Male']]
# df_female = df[df[['Genre'] == 'Feale']]

# df = df[df['Genre'] == 'Male']
# plt.scatter(df['Age'].tolist(), df['Annual Income (k$)'], color = 'red')
# plt.grid()
# plt.xlabel("Male Age")
# plt.ylabel('Annual Income (k$)')
# plt.show()

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
x = np.arange(10)
y1 = np.random.randint(3, 20, len(x))
w = 0.1
ax.bar(x - w/2, y1, width=w)
ax.bar(x + w/2, x, width=w)
plt.ylabel('Annual Income (k$)')
plt.xlabel('Genre')
plt.grid()
plt.show()