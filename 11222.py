import re

num = str(input('Введите номер телефона '))
r = re.compile('(\+7)\s[(]\d{3}[)]\s\d{3}\D*\d{2}\D*\d{2}')

if not(r.search(num)):
    while not(r.search(num)):
        print('не соответствует')
        num = str(input('Введите номер телефона '))
    print('соответствует')
else:
    print('соответствует')


