'''
s = [1, 2, 3, 4, 6]
print(sum(s)/len(s) if s else print())
 действие 1 if условие else действие не выполняется 

try:
    print(s)
except:
    print('0!')

'''

'''
a, b, c = float(input()), float(input()), float(input())
n = [1,2,3,4,5]
if a in n:
    print(a)
if b in n:
    print(b)
if c in n:
    print(c)



a = float(input())
b = float(input())
c = float(input())
d = (b**2-4*a*c)
print('Дискриминант = ', d)
if d == 0 and a != 0 and b != 0 and c != 0:
    print('Количество корней = 1')
    print('x1 = ', (-b)/2*a)
elif d == 0 and a == 0 and b == 0 and c == 0:
     print('Количество корней = бесконечности')
elif d < 0:
    print('Количесвто корней = 0')
elif d > 0:
    print('Количесвто корней = 2')
    print('x1 = ', (-b+d**0.5)/2*a)
    print('x_2 = ', (-b-d**0.5)/2*a)
else:
    print('Корней нет')

'''

n = int(input())
for i in range(n):
    if i%10 == 1 and i != 11:
        print(i, "Дамиль")
    if (i%10 == 2 or i%10 == 3 or i%10 == 4) and (1 <= i < 10):
        print(i, "Дамиля")
    if (i%10 == 2 or i%10 == 3 or i%10 == 4) and (i > 20):
        print(i, "Дамиля")
    if (5 <= i < 21):
        print(i, "Дамилей")  
    if (i > 21) and i%10 == 5:
        print(i, "Дамилей")  