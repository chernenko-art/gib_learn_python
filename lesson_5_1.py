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
# ru_string = 'Ну что ж я, я найти решения правильного не смогу ж? Смогу ж конечно, я ж старательный все ж таки.'
# en_string = 'Some some? english, text TEXT text.'
# arabic_string = 'يولد جميع الناس حراراً ,متساوين في الكرامة و,الحقوق.'

user_text = input("Введите текст:\n")


def check_text_is_eng(text):
    text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
    new_text_data = re.sub('[a-zA-Z\d+_]', '', text_without_punctuation)
    if re.search("\w", new_text_data):
        raise Exception("Only English supported!")


def encoder(text):
    pass


def decryptor(text):
    pass


def main(text):
    check_text_is_eng(text)
    encoder_text = encoder(text)
    print("encoder_text:\n", encoder_text)
    print("decryptor_text:\n", decryptor(encoder_text))


if __name__ == "__main__":
    main(user_text)