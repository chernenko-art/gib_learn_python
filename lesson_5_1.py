# "Привет. Сегодня пишем шифратор и дешифратор текста :)
# Работать будем только с английским. Следовательно, буквы будут использоваться только английского словаря.
#
# Надо написать две функции.
#
# Первая должна получать на вход строку и шифровать ее по следующему принципу - каждая буква заменяется на следующую в алфавите, при этом большая буква
# становится маленькой, а маленькая - большой.
# То есть ""a"" заменяется на ""B"", а ""X"" заменяется на ""z"". Последняя буква заменяется на первую, то есть ""Z"" на ""a"", а ""z"" на ""A"".
# Итоговая строка возвращается.
#
# Вторая функция должна расшифровывать строку, соответственно действовать наоборот."


import re
import string

# test_data
# user_text = 'A simpLe teXt in English To cheCk the tasK'

user_text = input("Введите текст:\n")


def check_text_is_eng(text):
    new_text_data = re.sub('[a-zA-Z]', '', text)
    if re.search("\w", new_text_data):
        raise Exception("Only English letters supported!")


def replace_on_next_letter(text):
    new_string = ''
    for symbol in text:
        if symbol.isalpha():
            ascii_code = ord(symbol)
            new_letter = chr(ascii_code + 1)
            new_string += new_letter
        else:
            new_string += symbol
    return new_string


def replace_on_previous_letter(text):
    new_string = ''
    for symbol in text:
        if symbol.isalpha():
            ascii_code = ord(symbol)
            new_letter = chr(ascii_code - 1)
            new_string += new_letter
        else:
            new_string += symbol
    return new_string


def replace_text_register(text):
    new_string = ''
    for symbol in text:
        if symbol.isalpha():
            if symbol.isupper():
                new_string += symbol.lower()
            elif symbol.islower():
                new_string += symbol.upper()
        else:
            new_string += symbol
    return new_string


def encoder(text):
    return(replace_text_register(replace_on_next_letter(text)))


def decryptor(text):
    return(replace_text_register(replace_on_previous_letter(text)))


def main(text):
    check_text_is_eng(text)
    encoder_text = encoder(text)
    print("Base text: \nA simpLe teXt in English To cheCk the tasK")
    print("encoder_text:\n", encoder_text)
    print("decryptor_text:\n", decryptor(encoder_text))


if __name__ == "__main__":
    main(user_text)
