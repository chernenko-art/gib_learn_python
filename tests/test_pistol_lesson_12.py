import sys
import os
import time
import pytest

sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}/..")

from lesson_12_2 import PistolModern
from custom_exeptions.MyExeptions import LockedException, HeatException, OutOfMagazins


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
            pistol.shot_auto(1000)
        except LockedException as e:
            assert e
        else:
            assert False, "LockedException is not worked!"

    def test_heat_exception(self):
        pistol = PistolModern(locked_chance=0)
        try:
            pistol.shot_auto(41)
        except HeatException as e:
            assert e
        else:
            assert False, "HeatException is not worked!"

    @pytest.mark.parametrize("shot_num, sleep_time", [(1, 5), (1, 1), (2, 1), (1, 2)])  # temperature value: >20, <20, 20, 19, 21
    def test_normal_temperature(self, shot_num, sleep_time):
        pistol = PistolModern(locked_chance=0)
        pistol.shot_auto(shot_num)
        time.sleep(sleep_time)
        pistol.shot_auto(shot_num)
        assert pistol.current_temperature >= 20, "Normal temperature >= 20"

    def test_reload(self):
        pistol = PistolModern(locked_chance=0, max_temperature=1000)
        magazins = pistol.magazins
        pistol.shot_auto(16)
        assert pistol.magazins == magazins - 1, "Auto reload is worked"
        pistol.shot_auto(4)
        pistol.reload()
        assert pistol.bullets == 15, "Manual reload is worked"
