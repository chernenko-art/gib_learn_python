import time
import getpass
import requests
from tzlocal import get_localzone_name
import re


# "Итак, стартуем с небольшой задачки. В каждом языке программирования есть способ получить текущее время.
#
# Предлагаю написать программу, которая приветствует Вас следующим образом:
#
# C 00 часов до 04 часов включительно программа при запуске пишет - ""Доброй ночи, {username}""
# С 05 часов до 09 часов включительно программа при запуске пишет - ""Доброе утро, {username}""
# С 10 часов до 16 часов включительно программа при запуске пишет - ""Добрый день, {username}""
# С 17 часов до 23 часов включительно программа при запуске пишет - ""Добрый вечер, {username}""
#
# Само собой, {username} должен заменяться на Ваше имя."


username = getpass.getuser()


def hello_user(hour, name=username):
    if 0 <= hour < 5:
        print(f"Доброй ночи, {name}")
    elif 5 <= hour < 10:
        print(f"Доброе утро, {name}")
    elif 10 <= hour < 15:
        print(f"Добрый день, {name}")
    else:
        print(f"Добрый вечер, {name}")


def run_hello_local_time():
    current_hour = int(time.strftime("%H"))
    hello_user(hour=current_hour)


# "В задаче №1 мы получаем текущее время, указанное на компьютере. Это не так интересно, как получать его с какого-нибудь стороннего сервиса.
# В этой задаче предлагаю выбрать любой сервис времени, API которого вам нравится (например http://worldtimeapi.org/).
# Следует написать GET-запрос, используя HTTP-библиотеку вашего языка (например, requests для Python или Apache HTTP Client для Java) и получить текущее время с учетом вашего UTC.
#
# В остальном задача выглядит аналогично. Надо написать программу, которая приветствует Вас следующим образом:
#
# C 00 часов до 04 часов включительно программа при запуске пишет - """"Доброй ночи, {username}""""
# С 05 часов до 09 часов включительно программа при запуске пишет - """"Доброе утро, {username}""""
# С 10 часов до 16 часов включительно программа при запуске пишет - """"Добрый день, {username}""""
# С 17 часов до 23 часов включительно программа при запуске пишет - """"Добрый вечер, {username}""""
#
# Само собой, {username} должен заменяться на Ваше имя."


def run_hello_global_time():
    local_time_zone = get_localzone_name()

    api_data = requests.get(f"http://worldtimeapi.org/api/timezone/{local_time_zone}").json()
    api_datetime = api_data['datetime']
    api_time = re.search(r'\d\d:\d\d:\d\d', api_datetime)[0]
    api_hour = int(api_time[:2])

    hello_user(hour=api_hour)


def main():
    print("Функция получения локального времени:")
    run_hello_local_time()
    print("\nФункция получения глобального времени:")
    run_hello_global_time()


if __name__ == "__main__":
    main()
