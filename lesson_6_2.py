# "Ваша задачка чуть сложнее. Вы заранее не знаете, сколько цифр будет в числе. На вход функции может прийти 1, 242, 14435 или 324234234
#
# Функция должна вернуть TRUE в случае, если сумма цифр, стоящих на четных позициях равна сумме цифр, стоящих на нечетных позициях ИЛИ если все цифры,
# стоящие на четных позициях равны всем цифрам, стоящих на нечетных. Иначе вернуть FALSE.
#
# Примеры:
#
# 3443 - TRUE
# 222222 - TRUE
# 321654 - FALSE"


try:
    input_number = int(input("Введите любое число: \n"))
except ValueError as e:
    print('Введите числовое значение!')
    raise e


def list_of_digits(number):
    digits_list = []
    while number > 0:
        digits_list.append(number % 10)
        number //= 10
    return digits_list


def check_sum_of_digits(number):
    even_sum = 0
    odd_sum = 0
    digits_list = list_of_digits(number)
    for i in range(len(digits_list)):
        if i % 2 == 0:
            even_sum += digits_list[i]
        else:
            odd_sum += digits_list[i]
    if even_sum == odd_sum:
        return True


def check_odd_even_equal(number):
    even_list = []
    odd_list = []
    digits_list = list_of_digits(number)
    for i in range(len(digits_list)):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if even_list == odd_list:
        return True


def main(number):
    if check_sum_of_digits(number) or check_odd_even_equal(number):
        return True
    else:
        return False


if __name__ == "__main__":
    print(main(input_number))
