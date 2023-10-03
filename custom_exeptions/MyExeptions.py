class LockedException(Exception):

    def __str__(self):
        return "Ohhh.. Pistol is locked!"


class HeatException(Exception):

    def __str__(self):
        return "Pistol is very heat! Wait for the pistol to cool down."


class OutOfMagazins(Exception):

    def __str__(self):
        return "Out оf magazins!"


class BadFormatException(Exception):

    def __str__(self):
        return "The amount must be a multiple of 100!"


class BadSumException(Exception):

    def __str__(self):
        return "Not enough money to give out!"
