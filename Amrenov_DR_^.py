'''
Выведите на экран цифры вводимого с клавиатуры натурального числа, пропуская цифры 2 и 5
'''

c = list(input())
ans = []
for i in range(0, len(c)):
    if (c[i] != '2') and (c[i] != '5'):
        ans.append(c[i])
print(*ans, sep='')