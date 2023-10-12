'''
https://github.com/Damilka05

1. Вычислить и вывести на экран сумму кубов натуральных чисел от 1 до n включительно. 
Верхний предел должен вводиться с клавиатуры и не должен превышать числа 100.

2. Выведите на экран таблицу умножения чисел от одного до девяти.
'''
a = list('абвгдежзийклмнопрстуфхцчшщъыьэюя   ')
for i in range(7):
    print('\n--------------------\n|', a[i].upper(), a[i], '|', '|', a[i+1].upper(), a[i+1], '|', '|', a[i+2].upper(),
          a[i+2], '|', '|', a[i+3].upper(), a[i+3], '|', '|', a[i+4].upper(), a[i+4], '|', sep='', end="\n--------------------")
    del a[i+1]
    del a[i+1]
    del a[i+1]
    del a[i+1]

print()
print('or')

a = list('абвгдежзийклмнопрстуфхцчшщъыьэюя   ')
for i in range(7):
    print('--------------------\n|' if i == 0 else '|', a[i].upper(), a[i], '|', '|', a[i + 1].upper(), a[i + 1], '|', '|', a[i + 2].upper(),
          a[i + 2], '|', '|', a[i + 3].upper(), a[i + 3], '|', '|', a[i + 4].upper(), a[i + 4], '|', sep='',
          end="\n--------------------\n")
    del a[i+1]
    del a[i+1]
    del a[i+1]
    del a[i+1]

n = int(input())
total = 0
for i in range(1, n+1):
    total += i**3
print(total)

for i in range(1, 10):
    for j in range(1, 10):
        print("%4d" % (i*j), end=' ')
    print()

