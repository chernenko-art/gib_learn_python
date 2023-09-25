# "Привет. Сегодня суббота и задачка будет попроще. Давайте поработаем с числами? Надо написать функцию, которая на вход получает число, состоящее
# из двух цифр. Например 10, 44 или 38.
#
# Функция должна вернуть TRUE в случае, если первая цифра в числе равняется второй цифре в числе ИЛИ если сумма первой и второй цифр равна 10.
# Во всех остальных случаях должен вернуться FALSE.
#
# Примеры:
#
# 33 - TRUE
# 46 - TRUE
# 38 - FALSE"


try:
    input_number = int(input("Введите 2-значное число: \n"))
except ValueError as e:
    print('Введите числовое значение!')
    raise e


def main(number):
    whole_number = number // 10
    remainder = number % 10
    if whole_number == remainder:
        return True
    elif whole_number + remainder == 10:
        return True
    else:
        return False


if __name__ == "__main__":
    print(main(input_number))
