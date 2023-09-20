# "Сегодня поработаем с массивами. Давайте напишем функцию, которая на вход получает массив слов. Например:
#
# [""apple banana"", ""orange"", ""banana"", ""kiwi strawberry blueberry""]
#
# Видно, что в этом массиве в некоторых слотах затесалось сразу несколько слов. На выходе функция должна вернуть такой массив, где одно слово будет в каждом элементе:
#
# [""apple"", ""banana"", ""orange"", ""banana"", ""kiwi"", ""strawberry"", ""blueberry""]
#
# Словом считается любой набор символов, обособленный пробелами или началом/концом строки.
#
# "


import json
from json.decoder import JSONDecodeError


word_list = ["apple banana", "orange\navokado", "banana", "kiwi strawberry blueberry"]

try:
    user_list = input('Введите слова в формате списка или пропустите для использования тестового списка из задачи: \n')
    if user_list:
        word_list = json.loads(user_list)
except JSONDecodeError as e:
    print('Неверный формат списка! Был применен тестовый список: ["apple banana", "orange\navokado", "banana", "kiwi strawberry blueberry"]')


def words_splitter(some_list):
    new_list = []
    for string in some_list:
        if " " in string:
            new_list += string.split(" ")
        elif "\n" in string:
            new_list += string.split("\n")
        else:
            new_list.append(string)
    return new_list


def main(some_list):
    print(words_splitter(some_list))


if __name__ == "__main__":
    main(word_list)
