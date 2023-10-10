# "Сегодня задачка на массивы. Пишум функцию, которая на вход получает несортированный массив чисел. Функция должна вернуть TRUE в случае,
# если в массиве есть два числа - 13 и 41
# Иначе вернуть FALSE"


class SearchNum:

    @staticmethod
    def search_num(array):
        if 13 in array and 41 in array:
            return True
        else:
            return False

    # 19_2==============
    # У вас чуть сложнее. Функция получает два массива чисел. Она должна вернуть TRUE в случае, если каждая цифра из второго массива встречается
    # в первом массиве хотя бы раз. Иначе FALSE.

    @staticmethod
    def search_matching_num_two_array(array_1, array_2):
        result = False
        for i in array_2:
            result = True if i in array_1 else False
        return result


def main():
    print(SearchNum.search_num([1, 2, 40, 555, 13, 49, 53, 41, 324567]))
    print(SearchNum.search_matching_num_two_array([1, 2, 40, 555, 13, 49, 53, 41, 324567], [40, 13, 1]))


if __name__ == '__main__':
    main()
