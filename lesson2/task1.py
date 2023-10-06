# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
# системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
# создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
# в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
# оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
# через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().
#

#
#
#
#

import re, csv

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = []


def load_file():
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    def open_file(name_txt: str, line):
        with open(name_txt, 'r', encoding='cp1251') as file1:
            if line == 'Изготовитель системы':
                value = re.search(rf'{line}:.+?\n', file1.read()).group()
                os_prod_list.append(value.split()[2])
            if line == 'Название ОС':
                value = re.search(rf'{line}:.+?\n', file1.read()).group()
                os_name_list.append(value.split()[2])
            if line == 'Код продукта':
                value = re.search(rf'{line}:.+?\n', file1.read()).group()
                os_code_list.append(value.split()[2])
            if line == 'Тип системы':
                value = re.search(rf'{line}:.+?\n', file1.read()).group()
                os_type_list.append(value.split()[2])
            file1.close()


    def write_to_csv(file_name, main: list ):
        with open(file_name, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(main)
            print(f'Файл с именем {file_name} создан.')



    for line in headers:
        open_file('info_1.txt', line)
        open_file('info_2.txt', line)
        open_file('info_3.txt', line)



    main_data.append(['Изготовитель системы:', os_prod_list])
    main_data.append(['Название ОС:', os_name_list])
    main_data.append(['Код продукта:', os_code_list])
    main_data.append(['Тип системы:', os_type_list])

    write_to_csv('main_data.csv', main_data)



load_file()
