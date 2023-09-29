from lesson_12_2 import PistolModern
from MyExeptions.MyExeptions import LockedException, HeatException, OutOfMagazins


class TestPistol:
    def test_check_out_of_magazin_exeption(self):
        pistol = PistolModern()
        magazins = pistol.magazins
        try:
            for i in range(magazins + 1):
                pistol.reload()
        except OutOfMagazins as e:
            assert e
        else:
            assert False, "OutOfMagazins exeption is not worked!"

    def test_locked_exception(self):
        pistol = PistolModern()
        pistol.magazins = 1000
        pistol.max_temperature = 10000
        try:
            pistol.shot(1000)
        except LockedException as e:
            assert e
        else:
            assert False, "LockedException is not worked!"

    def test_heat_exception(self):
        pistol = PistolModern()
        pistol.locked_chance = 0
        try:
            pistol.shot(41)
        except HeatException as e:
            assert e
        else:
            assert False, "HeatException is not worked!"
