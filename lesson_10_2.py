# "Для вас сегодня то же самое, только приводить надо не к двоичной системе, а к любой. Разрядность передается вторым параметром.
#
# Например, на вход функции пришло число 43 и разрядность 8. Ответ должен быть: 53"

def main(num, digit):
    revert_binary_number = ""
    while num >= digit:
        residue = num % digit
        num = num // digit
        revert_binary_number += str(residue)
    return (revert_binary_number + str(num))[::-1]


if __name__ == "__main__":
    num = int(input("Введите десятичное число: \n"))
    digit = int(input("Введите разрядность: \n"))
    print(main(num, digit))
