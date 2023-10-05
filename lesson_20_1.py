# "Сегодня пишем функцию, которая ищет пути. Суть в следующем. На вход этой функции приходит массив из трех массивов. Каждый внутренний массив содержит
# три элемента. Получается поле три на три.
# Каждая клеточка может иметь одно из трех значений - зеленый (З), красный (К) или синий (С)
# Ваша задача - понять, есть ли путь из клетки 1х1 к клетке 3х3 так, чтобы мы не шли по диагонали и чтобы за всю дорогу ни разу не сменили цвет.
# То есть мы можем переступать на соседнюю клеточку только того же цвета, с которого начала на 1х1"

class PathSearch:

    def __init__(self, canvas):
        self.canvas = canvas
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
        step_up = (0, -1)
        step_left = (-1, 0)
        match_array = [[2, 2]]

        while match_array:
            current_x,  current_y = match_array.pop()
            if current_x == 0 and current_y == 0:
                return True

            for x, y in [step_up, step_left]:
                new_pos = self._try_step(x, y, current_x,  current_y)
                if new_pos:
                    match_array.append(new_pos)

        return False


def main():
    searcher = PathSearch([("К", "К", "З"), ("З", "К", "К"), ("С", "К", "К")])
    searcher.print_canvas()
    print(searcher.path_search())


if __name__ == '__main__':
    main()
