# "В качестве более сложной задачи мы к задаче номер 1 добавим еще немного методов:
#
# 8) Исправить все записи. Функция должна читать файл, анализировать - является ли пользователь на самом деле тином в текущей локации или нет,
# и при необходимости корректировать ему поле is_teen, перезаписывая файл.
# 9) Перевезти пользователя в текущую локацию. Локация приходит параметром. Если локация не одна из четырех - Россия, Япония, США, Тайланд -
# функция пишет, что не можно перевезти туда пользователя. Если страна из этих четырех - перевозит, меняя запись в файле и перепроверяя и
# корректирую поле is_teen при необходимости. Например, если мы пользователя, которому 18 лет, перевозим из РФ в США, он должен перестать считаться
# совершеннолетним.
# 10) Добавить страну. Да-да, выходит, что возраст совершеннолетия для страны надо хранить в каком-то конфиге, который можно дополнять.
# При вызове этого метода название страны приходит параметром, вторым параметром приходит возраст совершеннолетия. После добавления страны пользователей
# можно перевозить в эту страну также (метод 9)."


import json

county_adult_age = {
    'Thailand': 20,
    'USA': 21,
    'Japan': 20,
    'Russia': 18
}

county_list = ['Thailand', 'USA', 'Japan', 'Russia']


def _get_db_list(db_file_path):
    with open(db_file_path, "r") as f:
        return json.load(f)


class UserDs:
    def __init__(self, db_path):
        self.db_path = db_path
        self.new_db_path = "lesson_8_2" + db_path
        self.db = _get_db_list(db_path)
        self.id = 'id'
        self.name = 'name'
        self.fname = 'fname'
        self.county = 'county'
        self.age = 'age'
        self.is_teen = 'is_teen'

    def correct_all_records(self):
        db = self.db
        for i in db:
            if i[self.is_teen]:
                if county_adult_age[i[self.county]] < i[self.age]:
                    i[self.is_teen] = False
                    print(f"corrected_id: {i[self.id]}\n")
            else:
                if county_adult_age[i[self.county]] > i[self.age]:
                    i[self.is_teen] = True
                    print(f"corrected_id: {i[self.id]}\n")
        self._save_db_to_file(db)

    def _save_db_to_file(self, db):
        with open(self.new_db_path, "w+") as f:
            json.dump(db, f, indent=4)

    def relocate_user(self, user_id, county):
        db = self.db
        if county not in county_list:
            raise Exception(f"Couty must be in: {county_list}")
        for i in db:
            if i[self.id] == user_id:
                if i[self.age] < county_adult_age[county] and not i[self.is_teen]:
                    i[self.is_teen] = True
                    print(f"is_teen param changed on True")
                elif i[self.age] > county_adult_age[county] and i[self.is_teen]:
                    i[self.is_teen] = False
                    print(f"is_teen param changed on False")
                i[self.county] = county
                print(f"user {i[self.name]} {i[self.fname]} relocated to {county}")
        self._save_db_to_file(db)

    def append_county(self, new_county, teen_age):
        pass


def main():
    user_ds = UserDs(db_path="users_ds.json")
    # user_ds.correct_all_records()
    # user_ds.relocate_user(user_id=9, county="USA")


if __name__ == "__main__":
    main()
