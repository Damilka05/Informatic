'''
ДЗ
import math

def s(x, y, z):
  p = (x + y + z) / 2
  s = math.sqrt(p * (p - x) * (p - y) * (p - z))
  return s

lst = list()
for i in range (1, 4):
  print('Введите стороны ', i, '-го треугольника: ')
  a = int(input('a: '))
  b = int(input('b: '))
  c = int(input('c: '))
  lst.append(s(a, b, c))
for i in range(3):
  print('Площадь ', i, '-го треугольника ', lst[i])
if lst[0] == lst[1]:
  if lst[0] == lst[2]:
    print('Треугольники равновеликие')
else: print('Треугольники не равновеликие ')

'''

'''
Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. Длину массива и его элементы ввести с клавиатуры.
 В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.

 Даны две дроби A/B и C/D (A, B, C, D - натуральные числа). Составить программу деления дроби на дробь. 
 Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД.

 Задана окружность (x-a)^2 + (y-b)^2 = r^2 и точки P(p1, p2), F(f1, f2), L(l1, l2). 
 Выяснить и вывести на экран, сколько точек и какие лежить внутри окружности. Проверку сформировать в виде процедуры.
'''

# 1
# def z(s):
#     a[0], a[m-1] = a[m-1], a[0]
#     return a

# m = int(input('Длина массива'))
# a = []
# for i in range(m):
#     a.append(int(input()))
# print(a)
# print(z(m))

# def f(c, z):
#     if c == z:
#         return c
#     while c != z:
#         if c > z:
#             c = c - z
#             z = z
#         else:
#             z = z - c
#             c = c
#     return c

# a, b, a_1, b_1 = int(input()), int(input()), int(input()), int(input())
# c = a*b_1
# z = b*a_1
# print(c, z)
# print(f(c, z))
# print(c//f(c, z), '/', z//f(c, z))

def dl(x1, y1):
    return (x1**2+y1**2)**0.5

total = 0
x, y, a, b = int(input()), int(input()), int(input()), int(input())
r = ((x-a)**2+(y-b)**2)**0.5
for i in range(3):
    x1, y1 = int(input()), int(input())
    if dl(x1, y1) < r:
      total += 1
print('Количество точек, которые находятся внутри окружности', total)