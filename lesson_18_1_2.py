# "Сегодня пишем банкомат для Сбера. Они, хоть и айти-компания теперь, без нас-то не смогут :)
# Надо написать функцию, которая получает на вход сумму, которую банкомат должен выдать. Вернуться должен массив, описывающий - в каких банкнотах
# мы будем выдавать денежку.
# Номиналы возможны следующие - 100, 200, 500, 1000, 2000, 5000
# Вторым параметром приходит тип выдачи. Существует два типа - ""с разменом"" и ""крупными"". С разменом - это когда мы выдаем минимальными валютами.
# Крупными - когда выдаем минимальным количеством купюр.
# Гарантируется, что сумма придет кратной 100."

# 18_2 ===================

# "Вам, как всегда, ничего не гарантируется. :)
# Если сумма пришла не кратной 100, кидаем BadFormatException.
# А еще у вас будет третий параметр - список доступных купюр. Например:
# {
# ""100"" => 3,
# ""500"" => 2
# }
# Это значит, что в банкомате есть только три сотки и две пятисотки. И все :)
# Если запрошенную сумму выдать не получается, кидаем BadSumException."


from custom_exeptions.MyExeptions import BadFormatException
from custom_exeptions.MyExeptions import BadSumException


class SberBankomat:

    def __init__(self, one_hundred=None, two_hundred=None, five_hundred=None,one_thousand=None,
                 two_thousand=None, five_thousand=None):
        self.one_hundred = one_hundred
        self.two_hundred = two_hundred
        self.five_hundred = five_hundred
        self.one_thousand = one_thousand
        self.two_thousand = two_thousand
        self.five_thousand = five_thousand
        self.money_in_bankomat = {100: self.one_hundred, 200: self.two_hundred, 500: self.five_hundred,
                                  1000: self.one_thousand, 2000: self.two_thousand, 5000: self.five_thousand}
        self.hundreds_nominals = [100, 200, 500]
        self.thousands_nominals = [1000, 2000, 5000]

    def _check_money_in_bankomat(self, array_for_get_out):
        for i in array_for_get_out:
            for key, value in i.items():
                if self.money_in_bankomat[key] < value:
                    raise BadSumException
                else:
                    self.money_in_bankomat[key] -= value
        return array_for_get_out

    def _hundreds_counter(self, money):
        result = []
        while money != 0:
            count_array = {money // i: i for i in self.hundreds_nominals if money // i >= 1}
            result.append({count_array[min(count_array)]: min(count_array)})
            money -= count_array[min(count_array)] * min(count_array.keys())
        return result

    def _thousands_counter(self, money):
        result = []
        while money != 0:
            count_array = {money // i: i for i in self.thousands_nominals if money // i >= 1}
            result.append({count_array[min(count_array)]: min(count_array)})
            money -= count_array[min(count_array)] * min(count_array.keys())
        return result

    def give_my_money(self, money, out_type):
        if money % 100:
            raise BadFormatException
        if out_type in "с разменом":
            count_money = money // min(self.hundreds_nominals)
            result = [{min(self.hundreds_nominals): count_money}]
            return self._check_money_in_bankomat(result)
        else:
            if money < 1000:
                result = self._hundreds_counter(money)
                return self._check_money_in_bankomat(result)
            else:
                hundreds_sum = money % 1000
                thousand_sum = money - hundreds_sum
                result = self._hundreds_counter(hundreds_sum) + self._thousands_counter(thousand_sum)
                return self._check_money_in_bankomat(result)


def main():
    bankomat = SberBankomat(one_hundred=100, two_hundred=100, five_hundred=100, one_thousand=100,
                            two_thousand=100, five_thousand=100)
    print(bankomat.give_my_money(5_500, out_type="с разменом"))
    print(bankomat.give_my_money(150_300, out_type="крупными"))
    print("Осталось в банкомате: ", bankomat.money_in_bankomat)


if __name__ == '__main__':
    main()
