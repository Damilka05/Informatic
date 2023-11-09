import re

# re.search(pattern, string) 	            Найти в строке string первую строчку, подходящую под шаблон pattern;
# re.fullmatch(pattern, string) 	        Проверить, подходит ли строка string под шаблон pattern;
# re.split(pattern, string, maxsplit=0) 	Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;
# re.findall(pattern, string) 	            Найти в строке string все непересекающиеся шаблоны pattern;
# re.finditer(pattern, string) 	            Итератор всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты);
# re.sub(pattern, repl, string, count=0) 	Заменить в строке string все непересекающиеся шаблоны pattern на repl;
# match[0], match.group() 	                Подстрока, соответствующая шаблону
# match.start() 	                        Индекс в исходной строке, начиная с которого идёт найденная подстрока
# match.end() 	                            Индекс в исходной строке, который следует сразу за найденной подстрока

# os.getswd

num = input()
ans = re.search(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', num)
ans2 = re.search(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', num)
if ans2 != None:
    print('Такси')
else:
    print('Частные')




# match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
# print(match[0] if match else 'Not found') 
# # -> 23-12 
# match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 
# print(match[0] if match else 'Not found') 
# # -> Not found 
