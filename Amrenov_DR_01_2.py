'''
Заполнить массив случайными положительными и отрицательными целыми числами. Вывести его на экран. Удалить из массива все отрицательные ...
'''

import random

a = int(input())
s = []
ans = []
for i in range(a):
    s.append(random.randint(-10**8, 10**8))
print(s)
for j in range(len(s)):
    if s[j] >= 0:
        ans.append(s[j])
print(ans)