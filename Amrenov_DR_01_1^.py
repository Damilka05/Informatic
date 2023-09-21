'''
1. Вычислить и вывести на экран длину окружности и площадь круга одного и того же заданного радиуса R, 
который необходимо ввести с клавиатуры в сантиметрах. Результаты должны округляться до сотых.

2. Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных на экран до и после замены.

3. Вычислить и вывести на экран период колебания маятника длиной L с точностью до сотых. Для рассчетов использовать формулу 
T = 2π√(L/g), где g – ускорение свободного падения (9.81 м/c2). Значение длины маятника в метрах необходимо ввести с клавиатуры.

'''
import math

# задание №1
r = float(input())
c = round(2*r*math.pi, 2)
s = round(math.pi*r**2, 2)
print(c)
print(s)

# задание №2
x, y = 10, 55
x_2, y_2 = y, x
print(x, y)
print(x_2, y_2)

# задание №3
l = float(input())
t = round((2*math.pi*math.sqrt(l/9.81)), 2)
print(t)


'''
Уважаемый Максим Александрович! 
В названии файла нельзя поставить * (звездочку), поэтому поставил ^. Некоторые из группы 4931101/30001 сдеали также
'''