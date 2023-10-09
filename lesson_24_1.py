# "Сегодня пишем генератор случайных данных. Надо написать метод, который получает на вход длину
# ОТ и ДО (оба параметра типа INT). Возвращает метод случайно сгенеренную строку, длина который попадает
# в указанный промежуток.
# Гарантируется, что число ОТ будет меньше числа ДО, оба числа будут положительными.
# Параметры ОТ и ДО - включительные. То есть длина строки может равнять ОТ и ДО.
#
# Метод должен каждый раз возвращать новое значение, так что хардкодить не получится :)"

import random
import string


def main(start: int, stop: int):
    rand_len = random.randint(start, stop)
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(rand_len))


if __name__ == '__main__':
    print(main(1, 5))
