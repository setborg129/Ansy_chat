import json
from socket import socket, AF_INET, SOCK_STREAM
import time, sys
from utils import get_message, send_message
from common.variables import DEFAULT_PORT, RESPONSE, ACTION, PRESENCE, ERROR, TIME, USER, ACCOUNT_NAME
import Logs.server_log_config
import logging
from decor import Logs


# " Программа для сервера

SERVER_LOGGER = logging.getLogger('server')

@Logs
def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and message[USER][
        ACCOUNT_NAME] == "Guest":
        return {RESPONSE: 200}

    # SERVER_LOGGER.error(f'Ошибка сообещния {RESPONSE: 400 }')
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


try:
    if (sys.argv[1]) == '-p':
        listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        print(f"Сервер запущен по порту - {sys.argv[sys.argv.index('-p') + 1]}: Ожидаем подключение клиента !")
        SERVER_LOGGER.info(
            f"Сервер запущен по порту {sys.argv[sys.argv.index('-p') + 1]}: Ожидаем подключение клиента !")
    else:
        listen_port = DEFAULT_PORT
        print(f'Сервер запущен, умолчанию порт -  {listen_port}')
        SERVER_LOGGER.info(f"Сервер запущен, умолчанию порт -  {listen_port}")

    if listen_port > 65535 or listen_port < 1024:
        SERVER_LOGGER.error('Укажите порт больше 1024 но меньше 65535')
        raise ValueError

except IndexError:
    # print('Введите правильно адрес -p [<Port>]')
    listen_port = DEFAULT_PORT
    print(f'Сервер запущен, умолчанию порт -  {listen_port}')
    SERVER_LOGGER.debug(f"Сервер запущен, по умолчанию порт - {listen_port}")

except ValueError:
    print("Введите порт от 1024 до 65535")
    sys.exit(1)

# Создаем обьект серверного сокета.
# Сетевой, потоковый (TCP)
SERV_SOCK = socket(AF_INET, SOCK_STREAM)

# Связываем сокет с адресом и портом
# Именно через них клиент подключется к серверу
SERV_SOCK.bind(('', listen_port))

# listen - сокет готов к прослушиванию
# Метод принимает один аргумент
# Максимальное количество подключений в очереди
SERV_SOCK.listen(5)

try:
    while True:
        # принимаем подключение клиентов !
        CLIENT, client_addr = SERV_SOCK.accept()
        print(f"Получен запрос на сооединение от клиента {client_addr}, {CLIENT}")
        SERVER_LOGGER.info(f"Получен запрос на сооединение от клиента {client_addr}, {CLIENT}")
        TIMESTR = time.ctime(time.time()) + "\n"

        try:
            message_from_client = get_message(CLIENT)
            SERVER_LOGGER.info(f'сообщение от клиента - {message_from_client} \n')
            print(f'инфа от клиента - {message_from_client} \n')
            responce = process_client_message(message_from_client)
            send_message(CLIENT, responce)
            CLIENT.close()


        except (ValueError, json.JSONDecodeError):
            print("Принято не корректное сообщение от клиента !")
            # SERVER_LOGGER.error("Принято не корректное сообщение от клиента !")
            CLIENT.close()
        CLIENT.close()
finally:
    SERV_SOCK.close()
