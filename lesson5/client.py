import json
from socket import socket, AF_INET, SOCK_STREAM
import sys, time
from common.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, PRESENCE, TIME, USER, ACTION, ACCOUNT_NAME, RESPONSE, ERROR
from utils import send_message, get_message
import logging
import Logs.client_log_config

CLIENT_LOGGER = logging.getLogger('client')


def create_presence(acc_name='Guest'):
    msg_out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: acc_name
        }

    }
    CLIENT_LOGGER.debug(f'f Создан {PRESENCE} сообщение для пользователя { acc_name}')
    return msg_out


def process_an(message):
    # Функция разбивает ответ сервера.
    CLIENT_LOGGER.info(f"Сервер отвечает клиенту { message }")
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


# try:
#     if (sys.argv[1]) == '-a':
#         listen_ip = sys.argv[sys.argv.index('-a') + 1]
#     else:
#         listen_ip = DEFAULT_IP_ADDRES
#
# except IndexError:
#     print('Некоректно введен IP адресс или порт сервера   -a <[IP]> -p <[Port]>')
#     sys.exit(1)

# параметры порта
# try:
#     if (sys.argv[3]) == '-p':
#         listen_port = int(sys.argv[sys.argv.index('-p') + 1])
#     else:
#         listen_port = DEFAULT_PORT
#     if listen_port > 65535 or listen_port < 1024:
#         raise ValueError
#
# except IndexError:
#     print('Введите правильно адрес. IP [<Port>]')
#     sys.exit(1)
#
# except ValueError:
#     print("Введите порт от 1024 до 65535")
#     sys.exit(1)

try:
    while True:
        CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
        # print(f"Выбран порт - {listen_port}\n")
        print(f"Выбран порт - {DEFAULT_PORT}\n")
        CLIENT_LOGGER.info(f'Пользователь выбрал порт {DEFAULT_PORT}')

        # конектимся к серверу
        CLIENT_SOCK.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        CLIENT_LOGGER.info(f'Клиент подключился к серверу с адресом {DEFAULT_IP_ADDRESS} по порту: {DEFAULT_PORT}')
        # # отправляем сообщение на сервер
        message_to_server = create_presence()
        print(message_to_server)
        send_message(CLIENT_SOCK, message_to_server)

        try:
            # # Получаем сообщение от сервера.
            from_server = process_an(get_message(CLIENT_SOCK))
            print(f"Ответ от Сервера: {from_server}")
            CLIENT_LOGGER.info(f'Ответ от сервера: {from_server}')
            time.sleep(2)

        except (ValueError, json.JSONDecodeError):
            print('Не удалось декодировать сообщение сервера')
            CLIENT_LOGGER.critical('Не удалось декодировать сообщение сервера')
            sys.exit(1)

except ConnectionRefusedError:
    print('Нет сооединение с сервером, проверте параметры подключения.\n')
    CLIENT_LOGGER.critical('Нет сооединение с сервером, проверте параметры подключения.\n')
    sys.exit(1)

finally:
    CLIENT_SOCK.close()
