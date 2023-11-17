import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7, 7]
plt.rcParams["figure.autolayout"] = True
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('ƒ(x) = (x**β+α**β)/x**β')

def f(x):
   return (x**b+a**b)/x**b

a = 1
b = 1
x = np.arange(-10, 10, 0.5)
plt.plot(x, f(x), color='red')
plt.legend (('ƒ(x)', 'ƒ(x)'))
plt.grid()
plt.show()