# "Сегодня задача №2 не связана с первой задачей. Сегодня мы напишем функцию, которая снова на вход получает текст и ищет в нем слова паразиты.
# Словами-паразитами называются слова, которые встречаются в тексте >= N раз, где N - целочисленный параметр, который передается вторым параметром в функцию.
#
# Несколько правил:
# - Словом считается любой набор символов, обособленный слева и справа пробелами ИЛИ началом/концом строки.
# - Слова с разным регистром считаются одним и тем же словом. То есть предлог ""под"", который мы можем встретить в середине предложения и
# ""Под"" - в начале предложения - одно и то же слово.
# - Знаки препинания не учитываются. То есть ""привет."" и ""привет"" - это одно и то же слово.
#
# Гарантируется, что текст будет только на русском или английском языках.
#
# Результат вернуть JSON'ом, где ключи - слова-паразиты, а значение - количество раз, которое оно встречается.
#
# Пример:
#
# Дано:
#
# text: ""Ну что ж я, я найти решения правильного не смогу ж? Смогу ж конечно, я ж старательный все ж таки.""
# max_amount: 3
#
# Ответ:
#
# {
# ""я"":3,
# ""ж"":5
# }"

import re
import string


user_text = input("Введите текст:\n")

try:
    max_amount = int(input("Введите число для определения слов паразитов:\n"))
except ValueError as e:
    print('Введите числовое значение!')
    raise e


def check_text_is_ru_or_eng(text):
    if not re.search("[а-яА-ЯёЁ]", text) or not re.search("[a-zA-Z]", text):
        raise Exception("Поддерживаетя только русский или английский алфавит!")


def modify_string(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))


def words_splitter(text):
    return re.split(" |\n", text)


def match_counter(array):
    return {word: array.count(word) for word in array if array.count(word) >= max_amount}


def main(text):
    modified_text = modify_string(text)
    check_text_is_ru_or_eng(modified_text)
    words_list = words_splitter(modified_text)
    print(match_counter(words_list))


if __name__ == "__main__":
    main(user_text)
