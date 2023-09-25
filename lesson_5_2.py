# "А тут сегодня будем работать с соленым md5 и файлами.
#
# Нужно написать две функции.
#
# Первая принимает на вход строку, """"солит"""" ее и хеширует в md5 (да-да, он устарел, но для тренировки ничем не плох). Так как md5 не поддается
# обратной расшифровке, нужно в файлике рядом в любом удобном вам формате запоминать изначальную строку, соль и хеш. Будет круто, если соль будет
# динамической и меняться по какой-то логике в зависимости от строки.
#
# Вторая функция должна получать на вход хеш и искать его с нашем файле. Если такое хеш уже был однажды сгенерен, функция должна возвращать соль и
# изначальное значение. Иначе кидать исключение.

import json
import os
from hashlib import md5

# test_data
# user_text = 'qweasdzxc'
# user_hash = '11568c1fee7ae90832a3cb47ffdc600b'

user_text = input("Введите строку:\n")
user_hash = input("Введите хеш для поиска:\n")

db_file_path = 'password_database.json'
salt = 'MyUniqueSault'


def read_json_data_from_file(file):
    if not os.path.isfile(db_file_path):
        json_data = []
        with open(db_file_path, 'w+') as f:
            json.dump(json_data, f)
    else:
        with open(db_file_path, 'r') as f:
            json_data = json.load(f)
    return json_data


def hash_function(text):
    salt_text = text + salt
    md5_hash = md5(salt_text.encode()).hexdigest()
    data = {
        'user_text': user_text,
        'salt': salt,
        'md5_hash': md5_hash
    }

    db_data = read_json_data_from_file(db_file_path)
    db_data.append(data)

    with open(db_file_path, 'w') as f:
        json.dump(db_data, f, indent=4)


def search_hash(hash):
    db_data = read_json_data_from_file(db_file_path)

    for elem in db_data:
        if elem['md5_hash'] == hash:
            return elem['salt'], elem['user_text']

    raise Exception('Хеш не найден!')


def main(text):
    hash_function(text)
    salt, user_text = search_hash(user_hash)
    print("Хеш найден:\n", f"coль: {salt}\n", f"строка: {user_text}\n")


if __name__ == "__main__":
    main(user_text)
