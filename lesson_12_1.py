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

    def __init__(self):
        self.magazins = 10
        self.bullets = 15

    def shot(self, shot):
        while shot > 0 and self.magazins >= 0 and self.bullets != 0:
            self.bullets -= 1
            shot -= 1

            if self.bullets == 0:
                self.reload()

    def reload(self):
        if self.magazins == 0:
            raise Exception("OutOfMagazins")

        self.magazins -= 1
        self.bullets = 15

    def amount(self):
        return {"magazins": self.magazins, "bullets": self.bullets}


def test_shot_with_reload(class_object):
    print(f'======Start test_shot_with_reload=====')
    class_object.shot(shot=5)
    print(f'End shooting: {class_object.amount()}')
    print("User reload init")
    class_object.reload()
    print(f'End shooting: {class_object.amount()}')


def test_shot_without_reload(class_object):
    print(f'======Start test_shot_without_reload=====')
    class_object.shot(shot=100)
    print(f'End shooting: {class_object.amount()}')
    class_object.shot(shot=44)
    print(f'End shooting: {class_object.amount()}')


def main():
    pistol = Pistol()
    test_shot_without_reload(pistol)
    test_shot_with_reload(pistol)


if __name__ == "__main__":
    main()
