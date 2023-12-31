# "Сегодня мы играем в крестики-нолики. Но для того, чтобы в них играть, сначала придется их написать.
# Суть игры в следующем. Есть условное поле три-на-три, я предлагаю нумеровать клеточки следующим образом:
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Человек играет за крестики, то есть делает ход первым. Компьютер - за нолики. Когда ходит человек, программа должна просить ввести номер ячейки,
# на которое человек хочет поставить свой крестик. Если поле занято, компьютер должен просить ввести другое число. После хода человека программа должна
# вывести текущее состояние поля. Например, я решил поставить крестик на поле номер 5. Лог будет следующим:
#
# Человек поставил крестик на клетку 5.
#
# 1 2 3
# 4 X 6
# 7 8 9
#
# После этого компьютер спрашивает - это конец игры? Человеку надо ввести Y в случае, если кто-то победил или если на поле закончились свободные клеточки. В другом случае - N.
# Если ввели Y, игра заканчивается, программа останавливается. Иначе начинается ход компьютера.
#
# Компьютер выбирает поле по очень простому алгоритму - он занимает клеточку с наименьшею цифрой. То есть в нашем случае ходит на клеточку 1. Лог программы следующий:
#
# Компьютер поставил нолик на клетку 1.
#
# O 2 3
# 4 X 6
# 7 8 9
#
# Далее программа снова спрашивает, закончилась ли игра. Снова вводим Y или N. Если ввели Y - игра заканчивается. Иначе снова начинается ход человека,
# у которого программа снова должна спросить, на какую клетку он ходит.
#
# Важный момент - после каждого хода, человека или компьютера, нужно распечатывать текущее состояние поля.
#
# Задача решается при помощи массива из трех массивов. :)"

class Game:

    def __init__(self):
        self.canvas = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10"}

    def user_action(self):
        num = input("Select the field number:\n")
        while self.canvas[num] == "0" or self.canvas[num] == 'X':
            print("This field is busy!")
            num = input("Select the field number:\n")
        self.canvas[num] = "X"

    def computer_action(self):
        list_without_zero_x = [int(i) for i in self.canvas.keys() if self.canvas[i] != '0' and self.canvas[i] != 'X']
        self.canvas[str(min(list_without_zero_x))] = "0"

    def print_canvas(self):
        val_list = [value for value in self.canvas.values()]
        print(f"""
        {val_list[0]} {val_list[1]} {val_list[2]}
        {val_list[3]} {val_list[4]} {val_list[5]}
        {val_list[6]} {val_list[7]} {val_list[8]}\n""")

    def game_over_check(self):
        game_over = input("Game over? (y/n)\n")
        if game_over == "y":
            return True


def main():
    game = Game()

    while True:
        game.user_action()
        game.print_canvas()
        if game.game_over_check():
            break
        game.computer_action()
        game.print_canvas()
        if game.game_over_check():
            break


if __name__ == "__main__":
    main()
