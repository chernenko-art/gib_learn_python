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


class UserDs:
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.new_db_path = "lesson8_new_" + self.db_file_path
        self.county_adult_age_file_path = "lesson8_conty_adult_age.json"
        self.id = 'id'
        self.name = 'name'
        self.fname = 'fname'
        self.county = 'county'
        self.age = 'age'
        self.is_teen = 'is_teen'

    def _get_county_adult_age(self):
        with open(self.county_adult_age_file_path, "r") as f:
            return json.load(f)

    def _get_db_list(self):
        with open(self.db_file_path, "r") as f:
            return json.load(f)

    def _save_db_to_new_file(self, data):
        with open(self.new_db_path, "w+") as f:
            json.dump(data, f, indent=4)

    def correct_all_records(self):
        db = self._get_db_list()
        county_adult_age_json = self._get_county_adult_age()
        for i in db:
            if i[self.is_teen]:
                if county_adult_age_json[i[self.county]] < i[self.age]:
                    i[self.is_teen] = False
                    print(f"corrected_id: {i[self.id]}")
            else:
                if county_adult_age_json[i[self.county]] > i[self.age]:
                    i[self.is_teen] = True
                    print(f"corrected_id: {i[self.id]}")
        self._save_db_to_new_file(db)

    def relocate_user(self, user_id, county):
        db = self._get_db_list()
        county_adult_age_json = self._get_county_adult_age()
        if county not in list(county_adult_age_json.keys()):
            raise Exception(f"Relocation is not impossible! County must be in: {list(county_adult_age_json.keys())}")
        for i in db:
            if i[self.id] == user_id:
                if i[self.age] < county_adult_age_json[county] and not i[self.is_teen]:
                    i[self.is_teen] = True
                    print(f"is_teen param changed on True")
                elif i[self.age] > county_adult_age_json[county] and i[self.is_teen]:
                    i[self.is_teen] = False
                    print(f"is_teen param changed on False")
                i[self.county] = county
                print(f"user with id:{user_id} {i[self.name]} {i[self.fname]} relocated to {county}")
        self._save_db_to_new_file(db)

    def append_county(self, new_county, teen_age):
        county_adult_age_json = self._get_county_adult_age()
        county_adult_age_json[new_county] = teen_age
        with open(self.county_adult_age_file_path, 'r+') as f:
            json.dump(county_adult_age_json, f, indent=4)
        print(f"County {new_county} appended")


def main():
    user_ds = UserDs(db_file_path="lesson8_users_ds.json")

    print("\n8. Start the correct_all_records() function:")
    user_ds.correct_all_records()

    print("\n9. Start the relocate_user() function:")
    user_ds.relocate_user(user_id=9, county="USA")

    print("\n9. Start the relocate_user() function:")
    user_ds.relocate_user(user_id=13, county="Tagil")  # comment this line to test the next methods

    print("\n10. Start the append_county() function:")
    user_ds.append_county(new_county="Tagil", teen_age=5)

    print("\n10. Start the relocate_user() function:")
    user_ds.relocate_user(user_id=13, county="Tagil")


if __name__ == "__main__":
    main()
