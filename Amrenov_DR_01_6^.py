'''
Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива; 
максимальное значение среди элементов второй строки массива. Вывести полученные значения.

Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. 
Вывести оба массива.

Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей,
в которой суммы элементов во всех строках и столбцах одинаковы.

Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
'''
from random import randint


# 1

n = int(input('Задание 1. Введите размер '))
arr = list()
# input array
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(randint(0, 100))
    arr.append(brr)
# output array
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()

ans = 0

for i in range(n):
    if arr[i][2] > 0:
        ans = arr[i][2]
print(ans)
print(max(arr[1]))


# 2
print('Задание 2')
m, n = int(input('m: ')), int(input('n: '))
arr = list()
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(randint(-100, 100))
    arr.append(brr)
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()

for i in range(m):
    for j in range(n):
        if arr[i][j] > 0:
            arr[i][j] = 1
        else:
            arr[i][j] = 0

for i in range(m):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()



def f(a):
    n = sum(a[0])
    for i in range(1, len(a)):
        if n != sum(a[i]):
            return False
    for j in range(len(a)):
        m = 0
        for k in range(len(a[j])):
            m += a[k][j]
        if m != n:
            return False
    return True

arr = list()
n = int(input('Задание 3. Порядок матрицы n:'))
for i in range(n):
     brr = list()
     for i in range(n):
         brr.append(int(input()))
     arr.append(brr)

print(f(arr))


arr = list()
n = int(input('Задание 4. Порядок матрицы n:'))
for i in range(n):
     brr = list()
     for i in range(n):
         brr.append(int(input()))
     arr.append(brr)

f = True
for k in range(n):
    for l in range(1,n):
        if arr[k][l]!=arr[l][k]:
            f = False
            break
if f !=False:
    print('Матрица симметрична')
else:
    print('Обычная матрица')