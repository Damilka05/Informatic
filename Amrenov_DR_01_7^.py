'''
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, 
как и всех подкаталогов при помощи функции print_docs(directory).

Составьте программу - простейший редактор текстовых файлов. Алгоритм работы программы:
    Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt.
    Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
    Если строка пустая или спец. символ - программа сохраняет файл.
'''
import os

# 1
def print_docs(directory):
    for path, dirs, files in os.walk(directory):
        print(path)
    for file in files:
        print('    ', os.path.join(path, file))

directory = r'C:\Users\Hp\Desktop\1'
print(print_docs(directory))

# 2
def alg(file):
    s = str(input('Введите текст. PS. Если ввести пустую строку или #, то программа закончит свою работу ')) + '\n'
    while (s != '#' + '\n') and (s != "" + '\n'):
        my_file = open(file, "a+")
        my_file.write(s)
        s = str(input('Введите текст ')) + '\n'
        my_file.close()

file = str(input('Введите имя файла ')) + '.txt'
print(alg(file))
