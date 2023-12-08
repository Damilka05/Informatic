'''
Для каждой задачи необходимо:

    Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций), график каждой функции должен быть одного цвета для одного значения α и β.
    Подписать оси и заголовок
    Создать легенду
    Сохранить изображение в svg файл

    1. Построить в общих осях графики для:

    α=1,β=1
    α=2,β=1
    α=1,β=2
    
    3. Построить в общих осях графики для x<0.

На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. Так же нанесите на графики прямую f(x) = 0.
Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.. 

    4. Построить в общих осях графики для:

    α=1,β=0.5
    α=1,β=−0.5
    α=1,β=−1.5
    Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость
'''


from matplotlib import pyplot as plt
import numpy as np

def f(x, a, b):
    return ((x**b+a**b)/x**b)

def g(a, b, color):
    x = []
    y = []
    for i in range(-100, 100):
        if i==0:
            x.append(float(np.inf))
            y.append(float(np.inf))
            continue
        x.append(i)
        y.append(f(i, a, b))
    plt.plot(x, y, color = color)
plt.legend()

#1
g(1,1,'blue')
g(1,2,'red')
g(2,1,'green')
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title(r"Задание 1: $ƒ(x) = \frac{x^\beta+\alpha^\beta}{x^\beta}$")
plt.grid()

plt.legend(['α=1,  β=1', 'α=1, β=2', 'α=2, β=1'])
plt.show()

#3
g(1, 0.5, 'blue')
g(1, -0.5, 'red')
g(1, -1.5, 'green')
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title(r"Задание 3: $ƒ(x) = \frac{x^\beta+\alpha^\beta}{x^\beta}$")
plt.grid()

plt.legend(['α=1,  β=0.5', 'α=1, β=-0.5', 'α=1, β=-1.5'])
plt.show()

#4
g(1, 0.5, 'blue')
g(1, 0.8, 'blue')
g(1, -0.5, 'red')
g(1, -0.8, 'red')
g(1, -1.5, 'green')
g(1, -2.5, 'green')
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title(r"Задание 4: $ƒ(x) = \frac{x^\beta+\alpha^\beta}{x^\beta}$")
plt.grid()

plt.legend(['α=1,  β=0.5', 'α=1, β=0.8', 'α=1, β=-0.5', 'α=1, β=-0.8', 'α=1, β=-1.5', 'α=1, β=-2.5'])
plt.show()