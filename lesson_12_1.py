# "Сегодня пишем класс-пистолет.
#
# У пистолета есть магазин. В магазине может быть максимум 15 патронов. При этом у нас изначально 10 магазинов.
#
# Методы:
#
# shot() - производит выстрел. При этом в текущем магазине становится на один патрон меньше. Если в текущем магазине нет патронов, магазин
# автоматически меняется на новый, только после этого происходит выстрел.
#
# reload() - перезаряжаем магазин на новый. При этом если в старом магазине остались патроны, они теряются. Если нового магазина нет, бросается
# исключение OutOfMagazins. Старый магазин при этом не меняется, т.е. если в нем были патроны, они остаются.
#
# amount() - возвращается JSON, например: {""magazins"": 5, ""bullets"": 3} - это значит, что у нас есть еще 5 новых магазинов и три патрона в текущем."


class Pistol:

    def __init__(self, magazins=10, bullets=15):
        self.magazins = magazins
        self.bullets = bullets

    def shot(self, count):
        pass

    def reload(self):
        pass

    def amount(self):
        pass


def test_shot_with_reload(class_object, shot):
    class_object.shot(shot)
    class_object.amount()
    class_object.reload()
    class_object.amount()


def test_shot_without_reload(class_object, shot):
    class_object.shot(shot)
    class_object.amount()


def main():
    pistol = Pistol()
    test_shot_with_reload(pistol, shot=5)
    test_shot_without_reload(pistol, shot=15)
