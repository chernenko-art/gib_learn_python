# "Сегодня мы будем работать с цифрами. А именно - писать число прописью :)
# Задача очень простая, пишем на вход функцию, куда можно передать число от нуля до одного миллиарда.
# Функция должна написать прописью это число.
# Например - передали 1,344,321
# Ответ - Один миллион, триста сорок четыре тысячи, триста двадцать один"

# 17_2=================================

# "У вас все то же самое, только мы считаем котиков :)
# Например - передали 1,344,321
# Ответ - Один миллион, триста сорок четыре тысячи, триста двадцать один котик
# Или передали 13
# Ответ - Тринадцать котиков"


class NumWord:

    def __init__(self):
        self.one_digit = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
                          6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
        self.num_for_10_to_19 = {10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать",
                                 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать",
                                 18: "восемнадцать", 19: "девятнадцать"}
        self.decimals = {20: "двадцать", 30: "тридцать",
                         40: "сорок", 50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят",
                         80: "восемьдесят", 90: "девяносто"}
        self.hundreds = {100: "сто", 200: "двести", 300: "триста", 400: "четыреста",
                         500: "пятьсот", 600: "шестьсот", 700: "семьсот", 800: "восемьсот",
                         900: "девятьсот"}
        self.one_digit_thousands_prefix = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
                                           7: "семь", 8: "восемь", 9: "девять"}
        self.thousands_postfix = {0: "тысяч", 1: "тысяча", 2: "тысячи", 3: "тысячи", 4: "тысячи", 5: "тысяч", 6: "тысяч",
                                  7: "тысяч", 8: "тысяч", 9: "тысяч"}
        self.million_postfix = {0: "миллионов", 1: "миллион", 2: "миллиона", 3: "миллиона", 4: "миллиона", 5: "миллионов", 6: "миллионов",
                                7: "миллионов", 8: "миллионов", 9: "миллионов"}
        self.cats_postfix = {0: "котиков", 1: "котик", 2: "котика", 3: "котика", 4: "котика", 5: "котиков", 6: "котиков", 7: "котиков",
                             8: "котиков", 9: "котиков"}

    def hundreds_in_word(self, num):
        cats_postfix = num % 10
        if 0 <= num < 10:
            return self.one_digit[num] + " " + self.cats_postfix[cats_postfix]
        elif 10 <= num < 20:
            return self.num_for_10_to_19[num] + " " + self.cats_postfix[0]
        elif num in self.decimals:
            return self.decimals[num] + " " + self.cats_postfix[cats_postfix]
        elif 20 <= num < 100:
            remainder = num % 10
            whole = num - remainder
            return self.decimals[whole] + " " + self.one_digit[remainder] + " " + self.cats_postfix[cats_postfix]
        elif num in self.hundreds:
            return self.hundreds[num] + " " + self.cats_postfix[cats_postfix]
        else:
            remainder = num % 10
            remainder_decimals = num % 100
            whole = num - remainder_decimals
            whole_decimals = remainder_decimals - remainder
            return (self.hundreds[whole] + " " + self.decimals[whole_decimals] + " " + self.one_digit[remainder] + " " +
                    self.cats_postfix[cats_postfix])

    def thousands_in_word(self, num):
        remainder = num % 1000
        whole = num // 1000
        postfix = whole % 10
        if whole < 10:
            return self.one_digit_thousands_prefix[whole] + " " + self.thousands_postfix[postfix] + " " + self.hundreds_in_word(remainder)
        else:
            return self.hundreds_in_word(whole) + " " + self.thousands_postfix[postfix] + " " + self.hundreds_in_word(remainder)

    def million_in_word(self, num):
        remainder = num % 1_000_000
        whole = num // 1_000_000
        postfix = whole % 10
        return self.hundreds_in_word(whole) + " " + self.million_postfix[postfix] + " " + self.thousands_in_word(remainder)

    def num_in_word(self, num):
        if num < 1000:
            print(self.hundreds_in_word(num))
        elif 1000 <= num < 1_000_000:
            print(self.thousands_in_word(num))
        elif 1_000_000 <= num < 1_000_000_000:
            print(self.million_in_word(num))
        else:
            print("Вы ввели миллиард или больше (котики закончились)")


def main():
    num_word = NumWord()
    num_word.num_in_word(0)
    num_word.num_in_word(12)
    num_word.num_in_word(854)
    num_word.num_in_word(5_997)
    num_word.num_in_word(257_991)
    num_word.num_in_word(1_344_321)
    num_word.num_in_word(134_344_323)
    num_word.num_in_word(1_778_257_997)


if __name__ == '__main__':
    main()
