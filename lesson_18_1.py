# "Сегодня пишем банкомат для Сбера. Они, хоть и айти-компания теперь, без нас-то не смогут :)
# Надо написать функцию, которая получает на вход сумму, которую банкомат должен выдать. Вернуться должен массив, описывающий - в каких банкнотах
# мы будем выдавать денежку.
# Номиналы возможны следующие - 100, 200, 500, 1000, 2000, 5000
# Вторым параметром приходит тип выдачи. Существует два типа - ""с разменом"" и ""крупными"". С разменом - это когда мы выдаем минимальными валютами.
# Крупными - когда выдаем минимальным количеством купюр.
# Гарантируется, что сумма придет кратной 100."


class SberBankomat:

    def __init__(self):
        self.nominals = [100, 200, 500, 1000, 2000, 5000]

    def give_my_money(self, money):
        pass


def main():
    bankomat = SberBankomat()
    bankomat.give_my_money(5_550)


if __name__ == '__main__':
    main()