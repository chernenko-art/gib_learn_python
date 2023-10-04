# "Сегодня пишем функцию, которая ищет пути. Суть в следующем. На вход этой функции приходит массив из трех массивов. Каждый внутренний массив содержит
# три элемента. Получается поле три на три.
# Каждая клеточка может иметь одно из трех значений - зеленый (З), красный (К) или синий (С)
# Ваша задача - понять, есть ли путь из клетки 1х1 к клетке 3х3 так, чтобы мы не шли по диагонали и чтобы за всю дорогу ни разу не сменили цвет.
# То есть мы можем переступать на соседнюю клеточку только того же цвета, с которого начала на 1х1"

class PathSearch:

    def __init__(self, array_1, array_2, array_3):
        self.array_1 = array_1
        self.array_2 = array_2
        self.array_3 = array_3
        self.canvas = [self.array_1, self.array_2, self.array_3]

    def _print_canvas(self, canvas):
        for i in canvas:
            for j in i:
                print(j, end=" ")
            print()

    def path_search(self):
        self._print_canvas(self.canvas)


def main():
    searcher = PathSearch(["З", "К", "С"], ["З", "К", "С"], ["З", "К", "С"])
    searcher.path_search()


if __name__ == '__main__':
    main()
