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
        self.canvas[random.choice(list_without_zero_x)] = computer_marker

    def game_over_check_improved(self, user_marker):
        line_1 = set([self.canvas["1"]] + [self.canvas["2"]] + [self.canvas["3"]])
        line_2 = set([self.canvas["4"]] + [self.canvas["5"]] + [self.canvas["6"]])
        line_3 = set([self.canvas["7"]] + [self.canvas["8"]] + [self.canvas["9"]])
        column_1 = set([self.canvas["1"]] + [self.canvas["4"]] + [self.canvas["7"]])
        column_2 = set([self.canvas["2"]] + [self.canvas["5"]] + [self.canvas["8"]])
        column_3 = set([self.canvas["3"]] + [self.canvas["6"]] + [self.canvas["9"]])
        diag_1 = set([self.canvas["1"]] + [self.canvas["5"]] + [self.canvas["9"]])
        diag_2 = set([self.canvas["7"]] + [self.canvas["5"]] + [self.canvas["3"]])

        if len(set(self.canvas.values())) == 2:
            print("Draw!")
            return True
        elif len(line_1) == 1:
            self._check_winner(line_1, user_marker)
            return True
        elif len(line_2) == 1:
            self._check_winner(line_2, user_marker)
            return True
        elif len(line_3) == 1:
            self._check_winner(line_3, user_marker)
            return True
        elif len(column_1) == 1:
            self._check_winner(column_1, user_marker)
            return True
        elif len(column_2) == 1:
            self._check_winner(column_2, user_marker)
            return True
        elif len(column_3) == 1:
            self._check_winner(column_3, user_marker)
            return True
        elif len(diag_1) == 1:
            self._check_winner(diag_1, user_marker)
            return True
        elif len(diag_2) == 1:
            self._check_winner(diag_2, user_marker)
            return True

    def _check_winner(self, line, user_marker):
        if user_marker in line:
            print("You win!")
        else:
            print("You lose!")


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
