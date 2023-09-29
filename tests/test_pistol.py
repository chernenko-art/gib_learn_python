import sys
import os

sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}/..")

from lesson_12_2 import PistolModern
from MyExeptions.MyExeptions import LockedException, HeatException, OutOfMagazins


class TestPistol:
    def test_check_out_of_magazin_exeption(self):
        pistol = PistolModern()
        try:
            for i in range(pistol.magazins + 1):
                pistol.reload()
        except OutOfMagazins as e:
            assert e
        else:
            assert False, "OutOfMagazins exeption is not worked!"

    def test_locked_exception(self):
        pistol = PistolModern(magazins=1000, max_temperature=10000)
        try:
            pistol.shot(1000)
        except LockedException as e:
            assert e
        else:
            assert False, "LockedException is not worked!"

    def test_heat_exception(self):
        pistol = PistolModern(locked_chance=0)
        try:
            pistol.shot(41)
        except HeatException as e:
            assert e
        else:
            assert False, "HeatException is not worked!"
