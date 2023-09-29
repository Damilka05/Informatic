'''
1. Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, 
сообщая об ошибке в случае деления на ноль.
2. Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е. Сумму покупки 
ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки.
3. Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. 
Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.
'''
# 1
a, b = int(input()), int(input())
if b != 0:
    print(a/b)
else:
    print('Ошибка')

# 2
s = float(input())
if s > 20:
    print("Сумма покупки = ", round(s-(s/100*35), 2),
          " Скидка = ", round((s/100*35), 2))
else:
    print("Сумма покупки = ", round(s, 2), " Скидка = 0")

# 3_1
month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
         'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
m = int(input())
if 1 <= m <= 12:
    print(month[m-1])
else:
    print('Ошибка')
