# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по
# умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.


import chardet

def open_file():
    with open("test_file.txt", mode='rb') as f:
        for line in f:
            print(line)
            print(chardet.detect(line))
            print(line.decode('utf-8'))
    f.close()



open_file()