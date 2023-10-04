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


def main():
    print(SearchNum.search_num([1, 2, 40, 555, 13, 49, 53, 41, 324567]))


if __name__ == '__main__':
    main()
