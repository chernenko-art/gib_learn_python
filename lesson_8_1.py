# "Сегодня будем имитировать работу с базой данных. Только вместо базы данных у нас будет файл с JSON.
#
# Сам файл можно скачать отсюда - https://drive.google.com/file/d/1CbAYvkwlFdviNWoA8MPu-WrF42znhjV6/view
#
# Это небольшая база с пользователями, которая содержит следующие колонки - ID пользователя, имя, фамилия, возраст, текущая страна, и булевое значение
# — считается ли пользователь совершеннолетним в этой стране.
#
# Известно, что в разных странах совершеннолетие считается с разного возраста. В файле принимают участие четыре страны — Россия (с 18 лет),
# Япония (с 20 лет), США (с 21 года) и Тайланд (с 20 лет).
#
# Наша задача — написать класс, которые работает с этой базой. Он должен содержать следующие методы:
#
# 1) Получить всех пользователей из указанной страны. Страна приходит параметром.
# 2) Получить всех пользователей указанного возраста. Возраст приходит параметром.
# 3) Получить всех пользователей старше указанного возраста. Возраст приходит параметром.
# 4) Получить всех пользователей младше указанного возраста или равного ему. Возраст приходит параметром.
# 5) Получить всех совершеннолетних.
# 6) Получить всех тинов.
# 7) Найти все битые записи. Битые записи — это когда пользователь для текущей локации на самом деле должен быть совершеннолетним или тином, а в
# базе поле is_teen проставлено неправильно.
#
# Само собой, нужно спроектировать класс так, чтобы было как можно меньше дублирования в коде."


import json
from data.files_path import lesson8

county_adult_age = {
    'Thailand': 20,
    'USA': 21,
    'Japan': 20,
    'Russia': 18
}


def _get_db_list(db_file_path):
    with open(db_file_path, "r") as f:
        return json.load(f)


class UserDs:
    def __init__(self):
        self.users = _get_db_list(lesson8["db_file_path"])

    def get_all_users_from_county(self, county):
        return [user for user in self.users if user['county'] == county]

    def get_all_users_equal_age(self, age):
        return [user for user in self.users if user['age'] == age]

    def get_all_users_older_age(self, age):
        return [user for user in self.users if user['age'] > age]

    def get_all_users_younger_or_equal_age(self, age):
        return [user for user in self.users if user['age'] <= age]

    def get_all_adults(self):
        return [user for user in self.users if not user['is_teen']]

    def get_all_teens(self):
        return [user for user in self.users if user['is_teen']]

    def get_collisions(self):
        users = self.users
        collisions_list = [user for user in users if user['is_teen'] and county_adult_age[user['county']] < user['age']
                           or county_adult_age[user['county']] > user['age']]
        return collisions_list


def main():
    user_ds = UserDs()
    all_users_from_county = user_ds.get_all_users_from_county(county="Russia")
    all_users_equal_age = user_ds.get_all_users_equal_age(age=29)
    all_users_older_age = user_ds.get_all_users_older_age(age=29)
    all_users_younger_or_equal_age = user_ds.get_all_users_younger_or_equal_age(age=29)
    all_adults = user_ds.get_all_adults()
    all_teens = user_ds.get_all_teens()
    collisions = user_ds.get_collisions()
    print(f"""
all_users_from_county:\n{all_users_from_county}\n
all_users_equal_age:\n{all_users_equal_age}\n
all_users_older_age:\n{all_users_older_age}\n
all_users_younger_or_equal_age:\n{all_users_younger_or_equal_age}\n
all_adults:\n{all_adults}\n
all_teens:\n{all_teens}\n
collisions:\n{collisions}\n""")


if __name__ == "__main__":
    main()
