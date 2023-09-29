'''
Выведите на экран цифры вводимого с клавиатуры натурального числа, пропуская цифры 2 и 5
'''

c = list(input())
ans = []
for i in range(0, len(c)):
    if (c[i] != '2') and (c[i] != '5'):
        ans.append(c[i])
print(*ans, sep='')

from numdeclination import NumDeclination

n = int(input())
nd = NumDeclination()
for i in range(n):
    converted = nd.declinate(i, ["Дамиль", "Дамиля", "Дамилей"], type = 1) # Получаем конвертированное слово, 1 - набор падежей.
    print(converted.number, converted.word)