# r'C:\User\nikolay\my_photo.png' - абсолютный путь
# './my_photo.png' - относительный путь
# '../masha/masha_photo.png' - относительный путь

# import os
# path = os.getcwd()
# print(path)

# with open 'c...txt' as f:
#   f.write()

# os.path.basename 

# def read_last(lines, file):
#   '''
#   This function prints
#   a last of rows in file.
#   Last number is input from user.
#   '''
#   abstract_file = open(file, 'r', encoding='utf-8')
#   rows = abstract_file.readlines()
#   print(rows[lines:]) #Измените эту строку для корректного вывода текста
#   for row in rows[lines:]:
#      print(row)

# PATH_FILE = r'/content/files/text.txt'

# n = int(input('Input int positive number: '))
# file = open(PATH_FILE, 'r', encoding='utf-8')
# rows_number = len(file.readlines()) #Получаем объем файла в строках

# if n > 0 and n < rows_number:
#   read_last(n, PATH_FILE)

# 1
# def read_last(lines, file):
#   abstract_file = open(file, 'r', encoding='utf-8')
#   rows = abstract_file.readlines()
#   print(*rows[lines:])

# n = int(input('Input int positive number: '))
# path_file = r'./oct_lab_27.txt'
# file = open(path_file, 'r', encoding='utf-8')
# rows_number = len(file.readlines())

# if n > 0 and n < rows_number:
#   read_last(n, path_file)

# 2
import os

def print_docs(directory):
    for path, dirs, files in os.walk(directory):
        print(path)
    for file in files:
        print('    ', os.path.join(path, file))
    

directory = r'C:\Users\Hp\Desktop\1'

print(print_docs(directory))