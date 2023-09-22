# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# тип на кириллице.

import os, urllib.request, chardet, subprocess


def ping_url_unix_system(url):
    os.system("ping -c 2 " + url + ' -t 1')


def ping_url(url):
    ARGS = ['ping', url]
    YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)

    for line in YA_PING.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))


ping_url('yandex.ru')
ping_url('youtube.com')


ping_url_unix_system('yandex.ru')
ping_url_unix_system('youtube.com')
