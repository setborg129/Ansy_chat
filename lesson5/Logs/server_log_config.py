import logging
import os
import sys

import logging.handlers

# 1 Инициализация клиентского логера
SERVER_LOGGER = logging.getLogger('server')

# 2 Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, '../Logs/server.log')

# Log_file
PATH_time = os.path.dirname(os.path.abspath(__file__))
PATH_time = os.path.join(PATH_time, '../Logs/Logs_file/server.log')


# 3 Создать обработчик
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setLevel(logging.CRITICAL)

# 4 Создать обработчик который выводит сообщения в файл
FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')

# 5 создаём формировщик логов (formatter):
CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# 6 Подключить обькт Formatter к обработчику
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)

# 7 создаём потоки вывода логов
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH_time, encoding='utf-8', interval=1, when='M')

# 8 добавить обработчик к регистратору
SERVER_LOGGER.addHandler(FILE_HANDLER)
SERVER_LOGGER.addHandler(LOG_FILE)
SERVER_LOGGER.setLevel(logging.DEBUG)



if __name__ == '__main__':
    SERVER_LOGGER.critical('Критическая ошибка\n')
    SERVER_LOGGER.error('Ошибка\n')
    SERVER_LOGGER.debug('Отладочная информация\n')
    SERVER_LOGGER.info('Информационное сообщение\n')
