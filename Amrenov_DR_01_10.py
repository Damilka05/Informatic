'''
    1. Создать объект pandas Series из листа, объекта NumPy, и словаря
    2. Получить не пересекающиеся элементы в двух объектах Series
    3. Узнать частоту уникальных элементов объекта Series (гистограмма)
    4. Объединить два объекта Series вертикально и горизонтально
    5. Найти разность между объектом Series и смещением объекта Series на n

for me:
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
data – массив, словарь или скалярное значение, на базе которого будет построен Series;
index – список меток, который будет использоваться для доступа к элементам Series. Длина списка должна быть равна длине data;
dtype – объект numpy.dtype, определяющий тип данных;
copy – создает копию массива данных, если параметр равен True в ином случае ничего не делает.
'''

import pandas as pd
import numpy as np

#1
print('Задание 1')
my_series_list = pd.Series(['лист', 'sdsdsds', 525454])
print(my_series_list)
my_series_numpy = pd.Series(np.array([1.5, 2, 3, 2.55, 1]))
print(my_series_numpy)
my_series_slovar = pd.Series({'dict': 1, 'dictionary': 'словарь'})
print(my_series_slovar)
print()

# 2
print('Задание 2')
ser1 = pd.Series([1, 2, 3, 5, 8])
ser2 = pd.Series([4, 5, 6, 7, 8])
obs = np.union1d(ser1, ser2)
pov = np.intersect1d(ser1, ser2)
ans = []

for i in range(len(obs)):
    if obs[i] in pov:
        pass
    else:
        ans.append(obs[i])

print(pd.Series(ans))

#3
print('Задание 3')
data = 'abcdefgjijklmnopqrstuvwxyz'
len_series = 20
ind = np.random.randint(len(data), size=len_series)
s = pd.Series(np.take(list(data), ind))
ans = s.value_counts()
print(ans)

#4
print('Задание 4')
s1 = pd.Series(range(5))
s2 = pd.Series(list('abcde'))
vertical = pd.concat([s1, s2])
horizontal = pd.concat([s1, s2], axis=1)
print(vertical)
print('Я не знаю, как сделать правильную индексовку сверху... Подскажите, пожалуйста')
print(horizontal)

# 5
print('Задание 5')
n = int(input('Введите n для задания 5 '))
s = pd.Series([1, 2, 5, 6, 14, 18, 22, 57, 105])
ans = s.diff(periods=n)
print(ans)