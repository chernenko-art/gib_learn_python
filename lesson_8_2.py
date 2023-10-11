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
from data.files_path import lesson8


class UserDs:

    @staticmethod
    def _get_county_adult_age():
        with open(lesson8["county_adult_age_file_path"], "r") as f:
            return json.load(f)

    @staticmethod
    def _get_users():
        with open(lesson8["db_file_path"], "r") as f:
            return json.load(f)

    @staticmethod
    def _save_db_to_new_file(data):
        with open(lesson8["new_db_path"], "w+") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _correct(user, age_list):
        if user['is_teen'] and age_list[user['county']] < user['age']:
            user['is_teen'] = False
            print(f"corrected_id: {user['id']}")
        elif age_list[user['county']] > user['age']:
            user['is_teen'] = True
            print(f"corrected_id: {user['id']}")

    def correct_all_records(self, id=None):
        users = self._get_users()
        county_adult_age_json = self._get_county_adult_age()

        for user in users:
            self._correct(user, county_adult_age_json)

        self._save_db_to_new_file(users)

    def relocate_user(self, user_id, county):
        users = self._get_users()
        county_adult_age_json = self._get_county_adult_age()

        if county not in list(county_adult_age_json.keys()):
            raise Exception(f"Relocation is not impossible! County must be in: {list(county_adult_age_json.keys())}")

        for user in users:
            if user['id'] == user_id:
                self._correct(user, county_adult_age_json)
                user['county'] = county
                print(f"user with id:{user_id} {user['name']} {user['fname']} relocated to {county}")

        self._save_db_to_new_file(users)

    def append_county(self, new_county, teen_age):
        county_adult_age_json = self._get_county_adult_age()
        county_adult_age_json[new_county] = teen_age

        with open(lesson8["county_adult_age_file_path"], 'r+') as f:
            json.dump(county_adult_age_json, f, indent=4)

        print(f"County {new_county} appended")


def main():
    user_ds = UserDs()

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
