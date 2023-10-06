# "Сегодня пишем функцию, которая ищет пути. Суть в следующем. На вход этой функции приходит массив из трех массивов. Каждый внутренний массив содержит
# три элемента. Получается поле три на три.
# Каждая клеточка может иметь одно из трех значений - зеленый (З), красный (К) или синий (С)
# Ваша задача - понять, есть ли путь из клетки 1х1 к клетке 3х3 так, чтобы мы не шли по диагонали и чтобы за всю дорогу ни разу не сменили цвет.
# То есть мы можем переступать на соседнюю клеточку только того же цвета, с которого начала на 1х1"
# === 20_2
# У вас все то же самое, только поле может быть любого размера, необязательно 3х3. И у вас можно идти по диагонали.

class PathSearch:

    def __init__(self, canvas):
        self.canvas = canvas
        self. x_len = len(self.canvas[0]) - 1
        self.y_len = len(self.canvas) - 1
        self.start_pos_letter = self.canvas[0][0]

    def print_canvas(self):
        for i in self.canvas:
            for j in i:
                print(j, end=" ")
            print()

    def _try_step(self, x, y, current_x,  current_y):
        current_x += x
        current_y += y
        current_letter = self.canvas[current_y][current_x]

        if current_x >= 0 and current_y >= 0 and current_letter == self.start_pos_letter:
            return [current_x, current_y]
        else:
            return False

    def path_search(self):
        """Реализовал движение не сверху вниз, а наоборот от угловой нижней клетки к верхней"""

        step_up = (0, -1)
        step_left = (-1, 0)
        step_diag = (-1, -1)
        match_array = [[self.x_len, self.y_len]]

        while match_array:
            current_x,  current_y = match_array.pop()
            if current_x == 0 and current_y == 0:
                return True

            for x, y in [step_up, step_left, step_diag]:
                new_pos = self._try_step(x, y, current_x,  current_y)
                if new_pos:
                    match_array.append(new_pos)

        return False


def main():
    searcher = PathSearch([("К", "К", "К", "К"),
                           ("К", "К", "З", "З"),
                           ("К", "С", "К", "К"),
                           ("К", "К", "С", "К")
                           ])
    searcher.print_canvas()
    print(searcher.path_search())


if __name__ == '__main__':
    main()
