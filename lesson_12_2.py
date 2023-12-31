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
from custom_exeptions.MyExeptions import OutOfMagazins, HeatException, LockedException


class PistolModern(Pistol):

    def __init__(self, magazins=10, bullets=15, is_locked=False, locked_chance=10, normal_temperature=20, max_temperature=60):
        super().__init__(magazins, bullets)
        self.is_locked = is_locked
        self.locked_chance = locked_chance
        self.normal_temperature = normal_temperature
        self.max_temperature = max_temperature
        self.current_temperature = normal_temperature
        self.shot_time = time.time()

    def shot_auto(self, shot=1):

        """ This method can fire in bursts """

        while shot > 0:
            timer = time.time()
            time_diff = abs(self.shot_time - timer)

            if self.bullets == 0:
                self.reload()

            if self.current_temperature > self.normal_temperature and time_diff >= 1:
                temperature_dif = abs(self.current_temperature - time_diff)
                self.current_temperature = temperature_dif if temperature_dif >= self.normal_temperature else self.normal_temperature
                print(f"Lowed current_temperature on the {int(time_diff)} gradus, current_temperature: {int(self.current_temperature)}")

            if self.is_locked:
                raise LockedException
            elif self.current_temperature >= self.max_temperature:
                raise HeatException

            if self.current_temperature <= self.max_temperature:
                shot -= 1
                self.is_locked = (random.choices([True, False], weights=[self.locked_chance, 100 - self.locked_chance]))[0]
                self.shot_time = time.time()
                self.current_temperature += 1
                print(f"Shoot! current_temperature: {int(self.current_temperature)}")
                self.bullets -= 1

    def reload(self):
        if self.is_locked:
            self.is_locked = False
        if self.magazins == 0:
            raise OutOfMagazins
        self.magazins -= 1
        self.bullets = 15
        print(f"Reload! left magazins: {self.magazins}")


def sleep_between_sots(t):
    print(f"Sleep {t} seconds")
    time.sleep(t)


def shot_with_manual_reload(class_object):
    print(f'======Start shot_with_manual_reload=====')
    class_object.shot_auto(shot=5)
    print(class_object.amount())
    class_object.reload()
    print(class_object.amount())
    sleep_between_sots(5)
    class_object.shot_auto(shot=20)


def shot_without_reload(class_object):
    print(f'======Start shot_without_reload=====')
    class_object.shot_auto(shot=20)
    sleep_between_sots(5)
    class_object.shot_auto(shot=20)
    sleep_between_sots(5)
    class_object.shot_auto(shot=20)
    sleep_between_sots(5)
    class_object.shot_auto(shot=20)
    print(class_object.amount())


def main():
    pistol = PistolModern()
    shot_without_reload(pistol)
    shot_with_manual_reload(pistol)


if __name__ == "__main__":
    main()
