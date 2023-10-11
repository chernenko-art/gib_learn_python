# "Для тех, кто хочет посложнее, анализатор текста должен вести себя несколько иначе. Он должен получать на вход три параметра:
# анализируемый текст, максимально допустимую длину, список запрещенных слов. Результатом работы этой функции должен быть JSON, в котором будут
# следующие поля:
#
# - ""length"" - длина строки
# - ""pure_length"" - длина строки без учета пробелов
# - ""origin_text"" - текст, полученный на входе
# - ""pure_text"" - текст, в котором все запрещенные слова из списка была заменены на три звездочки
# - ""pure_short_text"" - текст из pure_text, обрезанный на максимальном символе. Если этот символ не последний, надо это показать, добавив многоточие в конец.
#
# Пример:
#
# Дано:
#
# text: «Не забывайте о том, что все великие волшебники в истории в свое время были такими же, как мы, – школьниками. Если у них получилось, то получится и у нас», – Гарри Поттер.
# maxlen: 35
# forbidden_words: [""волшебники"", ""Гарри Поттер""]
#
# Результат функции:
#
# {
# ""length"":171,
# ""pure_length"":140
# ""origin_text"":""«Не забывайте о том, что все великие волшебники в истории в свое время были такими же, как мы, – школьниками.
# Если у них получилось, то получится и у нас», – Гарри Поттер.""
# ""pure_text"":""«Не забывайте о том, что все великие *** в истории в свое время были такими же, как мы, – школьниками.
# Если у них получилось, то получится и у нас», – ***.""
# ""pure_short_text"":""Не забывайте о том, что все великие...""
# }"

import json
from json.decoder import JSONDecodeError


user_text = input("Введите текст:\n")
if not user_text:
    raise Exception("Пустая строка с текстом, введите текст.")

try:
    user_max_length = int(input("Введите максимальную длину текста:\n"))
except ValueError as e:
    print('Введите числовое значение!')
    raise e

try:
    words_exception = input('Введите список запрещенных слов в формате ["волшебники", "Гарри Поттер"]:\n')
    user_words_list = json.loads(words_exception) if words_exception else []
except JSONDecodeError as e:
    print('Неверный формат списка!')
    raise e

# test data
# user_text = '«Не забывайте о том, что все великие волшебники в истории в свое время были такими же, как мы, – школьниками. Если у них получилось, то получится и у нас», – Гарри Поттер.'
# user_max_length = 35
# user_words_list = json.loads('["волшебники", "Гарри Поттер"]')


def text_length_without_spaces(text):
    return len(text.replace(' ', ''))


def text_length_even_or_not(text):
    if len(text) % 2 == 0:
        return("Количество символов в тексте четное")
    else:
        return ("Количество символов в тексте нечетное")


def replace_forbidden_words(text, words_list):
    for word in words_list:
        text = text.replace(word, '***')
    return text


def pure_short_text(text, max_length, words_list):
    pure_text = replace_forbidden_words(text, words_list)
    if len(pure_text) > max_length:
        return pure_text[:max_length] + "..."
    else:
        return pure_text


def main(text, max_length, words_list):
    result_dict = {'length': len(text), 'pure_length': text_length_without_spaces(text),
                   'origin_text': str(text), 'pure_text': replace_forbidden_words(text, words_list),
                   'pure_short_text': pure_short_text(text, max_length, words_list)}
    print(result_dict)


if __name__ == "__main__":
    main(user_text, user_max_length, user_words_list)
