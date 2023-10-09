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


class ResultType(Enum):
    INTEGER = 1
    STRING = 2
    LIST = 3


def main(result_type, start, stop):
    pass


if __name__ == '__main__':
    main(ResultType.INTEGER, 1, 5)
