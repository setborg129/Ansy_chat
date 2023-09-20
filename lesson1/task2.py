# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

list_world = [b'class', b'function', b'method']

def conv_code(list_str):
    for word in list_str:
        print(word)
        print(type(word))
        print(len(f"{word}\n"))
conv_code(list_world)