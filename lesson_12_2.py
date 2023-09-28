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
import random
from lesson_12_1 import Pistol
from lesson_12_1 import test_shot_without_reload
from lesson_12_1 import test_shot_with_reload


class PistolModern(Pistol):

    def __init__(self):
        super().__init__()
        self.locked = random.choices([True, False], weights=[10, 90])
        self.normal_temperature = 20
        self.max_temperature = 60
        self.timer = time.perf_counter()

    def shot(self, shot_num):
        while shot_num > 0 and self.magazins >= 0 and self.bullets != 0:
            if self.locked[0]:
                self.locked = True
                raise Exception("LockedException")
            self.bullets -= 1
            shot_num -= 1

            if self.bullets == 0 and self.magazins != 0:
                self.magazins -= 1
                self.bullets = 15

    def reload(self):
        if self.locked:
            self.locked = random.choices([True, False], weights=[10, 90])
        if self.magazins == 0:
            raise Exception("OutOfMagazins")

        self.magazins -= 1
        self.bullets = 15


def main():
    pistol = PistolModern()
    print(pistol.locked)
    test_shot_without_reload(pistol, shot_num=100)
    # test_shot_with_reload(pistol, shot_num=5)


if __name__ == "__main__":
    main()

