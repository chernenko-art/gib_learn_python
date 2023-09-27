# "Для вас задачка чуть сложнее. Условия те же, но у человека в начале программы спрашивают, за кого он хочет играть. Можно ввести X,
# чтобы играть за крестики или ввести O - за нолики. Первыми ходят крестики, так что если человек выбрал нолики, первым ходит компьютер.
#
# Помимо этого, компьютер ходит на свободное поле случайным образом.
#
# Плюс, программа сама автоматически должна определить, закончилась ли игра или нет. Игра заканчивается, когда на поле кончаются свободные клеточки.
# Или когда кто-то победил - то есть когда нолики стоят три по горизонтали, либо три по диагонали, либо три по вертикали. Компьютер должен написать в
# конце причину, по которой игра закончилась:
#
# ""Человек победил"", ""Компьютер победил"", ""Ничья"""
#
# 1 2 3
# 4 5 6
# 7 8 9

import random
from lesson_9_1 import Game


class GameImproved(Game):

    def user_action_improved(self, user_marker):
        num = input("Select the field number:\n")
        while self.canvas[num] == "0" or self.canvas[num] == 'X':
            print("This field is busy!")
            num = input("Select the field number:\n")
        self.canvas[num] = user_marker

    def computer_action_improved(self, user_marker):
        print("Computer_action: ")
        if user_marker == "X":
            computer_marker = "0"
        else:
            computer_marker = "X"
        list_without_zero_x = [i for i in self.canvas.keys() if self.canvas[i] != '0' and self.canvas[i] != 'X']
        random_field = random.choice(list_without_zero_x)
        self.canvas[random_field] = computer_marker

    def game_over_check_improved(self, user_marker):
        if user_marker == "X":
            computer_marker = "0"
        else:
            computer_marker = "X"
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 9), (3, 6, 9),
                            (1, 5, 9), (7, 5, 3)]
        for combination in win_combinations:
            if all([self.canvas[str(i)] == user_marker for i in combination]):
                print("You win!")
                return True
            elif all([self.canvas[str(i)] == computer_marker for i in combination]):
                print("You lose!")
                return True


def main():
    game = GameImproved()
    game.print_canvas()
    user_marker = input("Select X or 0:\n")

    while True:
        if user_marker == "X":
            game.user_action_improved(user_marker)
        else:
            game.computer_action_improved(user_marker)
        game.print_canvas()
        if game.game_over_check_improved(user_marker):
            break
        if user_marker == "X":
            game.computer_action_improved(user_marker)
        else:
            game.user_action_improved(user_marker)
        game.print_canvas()
        if game.game_over_check_improved(user_marker):
            break


if __name__ == "__main__":
    main()
