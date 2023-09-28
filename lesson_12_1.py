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

    def shot(self, shot_num):
        while shot_num > 0 and self.magazins >= 0 and self.bullets != 0:
            self.bullets -= 1
            shot_num -= 1

            if self.bullets == 0 and self.magazins != 0:
                self.magazins -= 1
                self.bullets = 15
        #         print(f"magazin reloaded")
        #         print(f"left shot: {shot_num}, left magazins: {self.magazins}, left bullets: {self.bullets}\n")
        #
        # print(f"Finish shooting! left shot: {shot_num}, left magazins: {self.magazins}, left bullets: {self.bullets}")

    def reload(self):
        if self.magazins == 0:
            raise Exception("OutOfMagazins")

        self.magazins -= 1
        self.bullets = 15
        # print(f"left magazins: {self.magazins}, left bullets: {self.bullets}")


    def amount(self):
        return {"magazins": self.magazins, "bullets": self.bullets}


def test_shot_with_reload(class_object, shot_num):
    class_object.shot(shot_num)
    print(class_object.amount())
    class_object.reload()
    print(class_object.amount())


def test_shot_without_reload(class_object, shot_num):
    class_object.shot(shot_num)
    print(class_object.amount())


def main():
    pistol = Pistol()
    test_shot_without_reload(pistol, shot_num=144)
    test_shot_with_reload(pistol, shot_num=5)


if __name__ == "__main__":
    main()
