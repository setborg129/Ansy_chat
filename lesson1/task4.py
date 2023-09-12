# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).


list_word = ['разработка', 'администрирование', 'protocol', 'standard']


def conv_bytes(lst):
    for word in lst:
        word_bytes = str(word)
        print(word_bytes.encode('utf-8'))
        print(word_bytes.encode('utf-8').decode('utf-8'))
        print("\n")


conv_bytes(list_word)