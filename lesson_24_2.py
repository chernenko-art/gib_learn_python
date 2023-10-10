# "У вас генератор чуть сложнее. Он первым параметром получает ENUM - возвращаемый тип будет ли числом,
# строкой или массивом.
# Далее два параметра ОТ и ДО, которые работают следующим образом:
# Для строки это длина. То есть возвращаемая строка будет не короче значения ОТ, но и не длиннее значения ДО.
# Для числа это величина. Число должно быть случайным, но быть не больше числа ОТ и не меньше числа ДО.
# Дли массива — это количество элементов в нем. Элементы массива — случайные числа от 0 до 100. Элементов в
# массиве не меньше, чем ДО, но и не больше чем ДО.
# Вам, как всегда, ничего не гарантируется. ОТ и ДО могут быть как отрицательными (кидаем BadParamsException),
# так и ОТ может быть больше ДО, в этом случае просто меняем их местами."


from enum import Enum
import random
import string
from custom_exeptions.MyExeptions import BadParamsException


class ResultType(Enum):
    INTEGER = 1
    STRING = 2
    LIST = 3


def rand_int(start, stop):
    return random.randint(start, stop)


def rand_str(start, stop):
    rand_len = random.randint(start, stop)
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(rand_len))


def rand_list(start, stop):
    return [random.randint(1, 100) for _ in range(random.randint(start, stop))]


def check_num(start, stop):
    if start < 0 or stop < 0:
        raise BadParamsException
    if start > stop:
        start, stop = stop, start
    return start, stop


def main(result_type, start, stop):
    start, stop = check_num(start, stop)

    if result_type.value == 1:
        print(rand_int(start, stop))
    elif result_type.value == 2:
        print(rand_str(start, stop))
    else:
        print(rand_list(start, stop))


if __name__ == '__main__':
    main(ResultType.INTEGER, 5, 1)
    main(ResultType.STRING, 1, 5)
    main(ResultType.LIST, 1, 5)

    # main(ResultType.INTEGER, -5, 1)
