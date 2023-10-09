# Сегодня учимся парсить параметры консольной утилиты. Допустим, у нас есть утилита run, которая
# запускается из консоли с различными параметрами. Например:
# run --online-mode
# run --ip=132.223.324.454
# run --stable-mode --ip=129.22.341.11
# Наша задача - написать функцию, которая на вход получает параметры строкой. Например, вот такую строку:
# ""--stable-mode --ip=129.22.341.11""
# Функция должна разобрать эту строку и вернуть ассоциативный массив (словарь, хешмап), где ключом будет
# название параметра без двух символов тире в начале, а значением будет либо то, что указано через знак
# равно (как для параметра ip), либо True, если ключ используется без значения.
# Например, нам на вход пришла вот такая строка: ""--stable-mode --ip=129.22.341.11 --online-mode --port=4455""
# Ожидаемый результат:
# [
# ''ip"" => ""129.22.341.11"",
#  ""port"" => ""4455"",
# ""stable-mode"" => ""True"",
# ""online-mode"" => ""True""
# ]
# Гарантируется, что все параметры начинаются с двух символов -- и что после параметра идет либо символ
# равно и значение (не менее одного символа), либо следующий параметр."

# ==== lesson 22_2

# "У вас задача та же, только гарантируется куда меньше. Добавляются следующие возможные варианты:
# 1) Ключ начинается с одного символа тире, а не двух. Например: -p
# 2) Значение после ключа может идти не после знака равно, а после пробела. Например: -ip 123.324.33.43
# 3) После ключа может идти знак равно без значения. В этом случае у параметра должно быть значение False.
# Например: --port=
# 4) После ключа может идти через пробелы несколько значений. В этом случае функция должна кидать исключение
# CannotParseException. Например: -port 4355 5545
#
# Примеры:
# На вход: ""-p 1 --port 4444 -ip=123.333.444.555 --local-time --self=""
# Результат:
# [
# ""p"" => ""1"",
# ""port"" => ""4444"",
# ""ip"" => ""123.333.444.555"",
# ""local-time"" => ""True"",
# ""self"" => ""False""
# ]
# На вход: ""-p 1 --port 4444 -ip=123.333.444.555 --local-time --self= --value this is""
# Результат: исключение, так как после ключа --value идет два значения, разделенных пробелом"

import argparse
from custom_exeptions.MyExeptions import CannotParseException


def no_space_in_arg(value):
    if len(value) > 1:
        raise CannotParseException


parser = argparse.ArgumentParser()
parser.add_argument("--online-mode", action="store_true")
parser.add_argument("--stable-mode", action="store_true")
parser.add_argument("-ip", "--ip", nargs="+", type=str)
parser.add_argument("-p", "--port", nargs="+", type=str)


def main():
    args = parser.parse_args()

    no_space_in_arg(args.ip)
    no_space_in_arg(args.port)

    args_array = {"online-mode": args.online_mode,
                  "stable-mode": args.stable_mode,
                  "ip": args.ip[0] if args.ip else False,
                  "port": args.port[0] if args.port else False}

    print(args_array)


if __name__ == '__main__':
    main()

# example usage:
# 1. lesson_22_1_2.py --ip 192.168.21.34 --online-mode -p 23
# 2. lesson_22_1_2.py --ip 192.168.21.34 --online-mode -p 23 24 -> exception
