# "Сегодня пишем банкомат для Сбера. Они, хоть и айти-компания теперь, без нас-то не смогут :)
# Надо написать функцию, которая получает на вход сумму, которую банкомат должен выдать. Вернуться должен массив, описывающий - в каких банкнотах
# мы будем выдавать денежку.
# Номиналы возможны следующие - 100, 200, 500, 1000, 2000, 5000
# Вторым параметром приходит тип выдачи. Существует два типа - ""с разменом"" и ""крупными"". С разменом - это когда мы выдаем минимальными валютами.
# Крупными - когда выдаем минимальным количеством купюр.
# Гарантируется, что сумма придет кратной 100."


class SberBankomat:

    def __init__(self):
        self.hundreds_nominals = [100, 200, 500]
        self.thousands_nominals = [1000, 2000, 5000]

    def _hundreds_counter(self, money):
        result = []
        while money != 0:
            count_array = {money // i: i for i in self.hundreds_nominals if money // i >= 1}
            result.append({min(count_array): count_array[min(count_array)]})
            money -= count_array[min(count_array)] * min(count_array.keys())
        return result

    def _thousands_counter(self, money):
        result = []
        while money != 0:
            count_array = {money // i: i for i in self.thousands_nominals if money // i >= 1}
            result.append({min(count_array): count_array[min(count_array)]})
            money -= count_array[min(count_array)] * min(count_array.keys())
        return result

    def give_my_money(self, money, out_type):
        if out_type in "с разменом":
            count_money = money // min(self.hundreds_nominals)
            return [{min(self.hundreds_nominals): count_money}]
        else:
            if money < 1000:
                return self._hundreds_counter(money)
            else:
                hundreds_sum = money % 1000
                thousand_sum = money - hundreds_sum
                return self._hundreds_counter(hundreds_sum) + self._thousands_counter(thousand_sum)


def main():
    bankomat = SberBankomat()
    print(bankomat.give_my_money(5_500, out_type="с разменом"))
    print(bankomat.give_my_money(150_300, out_type="крупными"))


if __name__ == '__main__':
    main()
