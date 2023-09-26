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
    def __init__(self, db_path):
        self.db = _get_db_list(db_path)
        self.id = 'id'
        self.name = 'name'
        self.fname = 'fname'
        self.county = 'county'
        self.age = 'age'
        self.is_teen = 'is_teen'

    def _db_searching(self, key, value, older=None, younger=None):
        new_array = []
        db = self.db
        for i in db:
            if older:
                if i[key] > value:
                    new_array.append(i)
            elif younger:
                if i[key] <= value:
                    new_array.append(i)
            else:
                if i[key] == value:
                    new_array.append(i)
        return new_array

    def get_all_users_from_county(self, county):
        return self._db_searching(key=self.county, value=county)

    def get_all_users_equal_age(self, age):
        return self._db_searching(key=self.age, value=age)

    def get_all_users_older_age(self, age):
        return self._db_searching(key=self.age, value=age, older=True)

    def get_all_users_younger_or_equal_age(self, age):
        return self._db_searching(key=self.age, value=age, younger=True)

    def get_all_adults(self, is_teen=False):
        return self._db_searching(key=self.is_teen, value=is_teen)

    def get_all_teens(self, is_teen=True):
        return self._db_searching(key=self.is_teen, value=is_teen)

    def get_collisions(self):
        collisions_list = []
        db = self.db
        for i in db:
            if i[self.is_teen]:
                if county_adult_age[i[self.county]] < i[self.age]:
                    collisions_list.append(i)
            else:
                if county_adult_age[i[self.county]] > i[self.age]:
                    collisions_list.append(i)
        return collisions_list


def main():
    user_ds = UserDs(db_path="users_ds.json")
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
