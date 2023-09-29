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


class PistolModern(Pistol):

    def __init__(self):
        super().__init__()
        self.locked = random.choices([True, False], weights=[10, 90])
        self.normal_temperature = 20
        self.max_temperature = 60
        self.current_temperature = 20
        self.shot_time = time.time()

    def shot(self, shot):
        while shot > 0 and self.magazins >= 0 and self.bullets != 0:
            timer = time.time()
            time_difference = int(abs(self.shot_time - timer))

            if self.current_temperature > self.normal_temperature and time_difference >= 1:
                self.current_temperature -= time_difference
                print(f"Lowed current_temperature on the {time_difference} gradus, current_temperature: {self.current_temperature}")

            if self.locked[0]:
                self.locked = True
                raise Exception("LockedException")

            if self.current_temperature >= 60:
                raise Exception("HeatException")

            if self.current_temperature <= self.max_temperature:
                shot -= 1
                self.shot_time = time.time()
                self.current_temperature += 1
                print(f"Shoot! current_temperature: {self.current_temperature}")
                self.bullets -= 1

            if self.bullets == 0:
                self.reload()

    def reload(self):
        if self.locked:
            self.locked = random.choices([True, False], weights=[10, 90])
        if self.magazins == 0:
            raise Exception("OutOfMagazins")
        self.magazins -= 1
        self.bullets = 15
        print(f"Reload! left magazins: {self.magazins}")


def sleep_between_sots(t):
    print(f"Sleep {t} seconds")
    time.sleep(t)


def test_shot_with_reload(class_object):
    print(f'======Start test_shot_with_reload=====')
    class_object.shot(shot=5)
    print(class_object.amount())
    class_object.reload()
    print(class_object.amount())
    sleep_between_sots(5)
    class_object.shot(shot=20)


def test_shot_without_reload(class_object):
    print(f'======Start test_shot_without_reload=====')
    class_object.shot(shot=20)
    sleep_between_sots(5)
    class_object.shot(shot=20)
    sleep_between_sots(5)
    class_object.shot(shot=20)
    sleep_between_sots(5)
    class_object.shot(shot=20)
    print(class_object.amount())


def main():
    pistol = PistolModern()
    test_shot_without_reload(pistol)
    test_shot_with_reload(pistol)


if __name__ == "__main__":
    main()
