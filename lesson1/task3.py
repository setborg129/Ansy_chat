# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


# w1 = b'attribute'
# w2 = b'класс'
# w3 = b'функция'
# w4 = b'type'
word_list = ('attribute', 'класс', 'функция', 'type')

def write_bytes(lst_wrd):
    result_list = []
    new_bytes = ''
    for word in lst_wrd:
        # try:
        new_bytes = "b'" + word
        # except TypeError:
        #     continue

        result_list.append(new_bytes)
    print(result_list)
    print(type(result_list))
    for r in result_list:
        print(type(r))


write_bytes(word_list)
