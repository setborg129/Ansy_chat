# ### 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# # Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
import json

data_db = dict


def write_order_to_json():
    # передаем товар (item), количество (quantity), # цена (price), покупатель (buyer), дата (date).

    data_db = {
        'item': 'notebook',
        'quantity': 1,
        'price': 85000,
        'buyer': 'Human',
        'date': '01.01.2023',
    }

    with open('orders.json', 'w') as f:
        f.write(json.dumps(data_db, indent=4))

    with open('orders.json', 'r', encoding='cp1251') as file:
        files = json.loads(file.read())
        print(files)

write_order_to_json()
