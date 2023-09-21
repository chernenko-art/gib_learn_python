# "Для вас задачка чуть сложнее. Мы должны сделать все то же самое, что описано в задаче №1. Но за линейное время.
# Для тех, кто незнаком с оценкой сложности алгоритмов можно почитать вот эти статьи:
#
# Введение в анализ сложности алгоритмов (часть 1) - https://habr.com/ru/post/196560/
#
# Введение в анализ сложности алгоритмов (часть 2) - https://habr.com/ru/post/195482/
#
# Введение в анализ сложности алгоритмов (часть 3) - https://habr.com/ru/post/195996/
#
# Введение в анализ сложности алгоритмов (часть 4) - https://habr.com/ru/post/196226/"

import json
from json import JSONDecodeError


try:
    input_str = input("Введите массив чисел в формате списка: \n")
    input_list = json.loads(input_str)
except JSONDecodeError as e:
    print('Неверный формат списка!')
    raise e

try:
    input_number = int(input("Введите число: \n"))
except ValueError as e:
    print('Введите числовое значение!')
    raise e


# array: [1, 3, 12, 11, 2]
# N: 5
def main(array, number):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == number:
            return True
        if current_sum < number:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(main(input_list, input_number))
