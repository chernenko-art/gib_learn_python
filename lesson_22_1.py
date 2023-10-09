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
#
# [
# ''ip"" => ""129.22.341.11"",
#  ""port"" => ""4455"",
# ""stable-mode"" => ""True"",
# ""online-mode"" => ""True""
# ]
#
# Гарантируется, что все параметры начинаются с двух символов -- и что после параметра идет либо символ
# равно и значение (не менее одного символа), либо следующий параметр."

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--online-mode", action="store_true")
parser.add_argument("--stable-mode", action="store_true")
parser.add_argument("--ip", type=str)
parser.add_argument("--port", type=str)


def main():
    args = parser.parse_args()
    args_array = {"online-mode": args.online_mode,
                  "stable-mode": args.stable_mode
                  }
    if args.ip:
        args_array["ip"] = args.ip
    if args.port:
        args_array["port"] = args.port

    print(args_array)


if __name__ == '__main__':
    main()
