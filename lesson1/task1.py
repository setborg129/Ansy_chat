# Задание 1
# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных.
#    Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
# также проверить тип и содержимое переменных.



string_word_1 = "разработка"
word_unicode_1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"

print(string_word_1)
print(type(string_word_1))
print(type(word_unicode_1))
print(f"{word_unicode_1}\n-------------\n")

string_word_2 = "сокет"
word_unicode_2 ="\u0441\u043e\u043a\u0435\u0442"
print(string_word_2)
print(type(string_word_2))
print(type(word_unicode_2))
print(f"{word_unicode_2}\n-------------\n")

string_word_3 = "декоратор"
word_unicode_3 = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
print(string_word_3)
print(type(string_word_3))
print(type(word_unicode_3))
print(f"{word_unicode_3}\n-------------\n")


word_all = [string_word_1, string_word_2, string_word_3]
def convecter_unicode(str_unicode):
    for word in str_unicode:
        word_encode = str(word.encode("unicode_escape"))
        print(word_encode.replace("b", ""))
        print(type(word_encode))

convecter_unicode(word_all)



