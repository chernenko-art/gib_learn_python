# "Вам надо реализовать дополнительные особенности:
#
# При выстреле может произойти осечка с 10% вероятностью. Пистолет попадает в состояние locked. Патрон при этом не тратится.
# Но все последующие вызовы shot() должны бросать исключение LockedException и не производить выстрела.
# Чтобы вывести пистолет из состояния locked, необходимо вызвать метод reload(), который заменит магазин на новый.
#
# Пистолет может перегреться. Нормальная температура пистолета - 20 градусов. Ниже нее пистолет опуститься не может.
# Каждый выстрел повышает температуру на 1 градус. При этом каждую секунду пистолет остывает на один градус, но не ниже нормальной (20 градусов).
# То есть если мы сделали три выстрела подряд, температура пистолета станет 23 градуса. Если мы потом подождем 1 секунду,
# температура опустится до 22 градусов. Если температура пистолета становится > 60 градусов, при попытке выстрелить происходит исключение
# HeatException, выстрел не происходит. После того как температура падает до 60 градусов и ниже, выстрелы снова становятся доступными.
#
# На класс надо написать юнит-тесты, которые будут проверять пограничные значения. Можно использовать юнитовый фреймворк
# (# PyTest для Python, JUnit или TestNG для Java и Kotlin, или Mocha + Chai для JS). Если не разберетесь, написать тесты просто
# последовательно вызывая нужные методы и оборачивая проверки в IF примерно так:  IF (EPXECTED_CONDITION) print(""All good"") ELSE print(""All bad"")"

import time
from lesson_12_1 import Pistol


class PistolModern(Pistol):

    def __init__(self):
        super().__init__()
        self.chance_of_failure = 0.1
        self.locked = False
        self.normal_temperature = 20
        self.max_temperature = 60
        self.timer = time.perf_counter()


def main():
    pass


if __name__ == "__main__":
    main()

