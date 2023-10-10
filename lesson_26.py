# Последняя задачка пусть будет простой - давайте напишем функцию, которая будет писать воздравление с новым годом в зависимости
# от возраста, пола и и имени человека. Все три параметра будут передаваться в функцию. Условия следующие:
#
# Шаблон сообщения:
# Уважаемый/Уважаемая {имя}. Поздравляю тебя/Вас с Новым годом. :)
# От пола зависит первое слово. Имя подставляется на второе место. А обращения ""тебя"" и ""Вас"" зависит от возраста. До 49 лет включительно
# мы на ты, дальше на Вы. :)


from custom_exeptions.MyExeptions import BadGenderException


def check_age(age):
    prefix = "тебя" if age <= 49 else "Вас"
    return prefix


def check_gender(gender):
    if gender == "М":
        return "Уважаемый"
    elif gender == "Ж":
        return "Уважаемая"
    else:
        raise BadGenderException


def main(age, gender, name):
    print(f"{check_gender(gender)} {name}. Поздравляю {check_age(age)} с Новым годом. :)")


if __name__ == '__main__':
    main(12, "М", "Васёк")
    main(50, "М", "Васёк")
    main(49, "Ж", "Ленок")
