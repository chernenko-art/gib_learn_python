# "Сегодня нас ждет несложная алгоритмическая задачка. Мы напишем функцию, которая на вход будет получать несортированный массив чисел
# первым параметром, и какой-то число вторым параметром.
#
# Функция должна вернуть TRUE в случае, если в массиве есть два числа, которые в сумме датю то, которое мы передали вторым параметром.
#
# Например
#
# array: [1, 3, 2, 12, 11]
# N: 5
#
# result: TRUE // так как 3 и 2 в сумме дают 5"

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


# array: [1, 3, 2, 12, 11]
# N: 5
def main(array, number):
    for i in range(len(array)-1):
        for num in array[i+1:]:
            if number == array[i] + num:
                return True


if __name__ == "__main__":
    print(main(input_list, input_number))
