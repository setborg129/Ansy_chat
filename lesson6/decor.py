# Реализация в виде функции

import sys
import logging
import traceback
import inspect
import Logs.client_log_config
import Logs.server_log_config

if (sys.argv[0]) == 'server.py':
    LOGGER = logging.getLogger('server')
    print(f'Выбрали сервер')
elif (sys.argv[0]) == 'client.py':
    LOGGER = logging.getLogger('client')
    print(f'Выбрали Клиент !')

def Logs(func_to_log):
    # Функция - декаратор  """"
    print('Logs')

    def log_server(*args, **kwargs):
        print('args, kwargs')
        # """"""" Обертка """""""
        ret = func_to_log(*args, **kwargs)
        print('func_to_logs')
        LOGGER.debug(
            f'Была вызвана функция {func_to_log.__name__}, c параметрами {args} и {kwargs}.'
            f'Вызов из модуля {func_to_log.__module__}. Вызов из '
            f'Функции {traceback.format_stack()[0].strip().split()[-1]}.'
            f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2)
        return ret

    return log_server
