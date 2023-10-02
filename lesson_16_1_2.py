# "Сегодня будет писать небольшую очередь. Надо создать класс, у которого будет три метода - add(), getLast() и getFirst()
#
# При вызове add() мы должны передать в него любое число, которое класс ""запомнит"". Например, мы передаем 5 и класс запоминает это число как первое.
# Затем снова вызываем add(6) и класс запоминает это число, как второе.
# При вызове getLast() класс должен вернуть последнее добавленное число и ""забыть"" его. Например, в нашем случае вернуть 6. Если вызвать метод еще раз,
# вернется 5. А затем NULL.
# При вызове getFirst() класс работает наоборот. Возвращает самое ранее добавленное число и забывает его. В нашем случае снала 5, затем 6.
# Если в классе кончились числа, класс должен вернуть NULL на вызов и getLast() и getFirst()."


class Queue:

    def __init__(self):
        self.queue = []

    def add(self, num):
        self.queue.append(num)

    def get_last(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None

    def get_first(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

# "Вам надо расширить этот класс следующими методами:
# append() - в отличие от add() добавляет число в начало очереди, а не в конец.
# reverse() - переворачивает очередь - последнее число становится первым, первое - последним."

    def append(self, num):
        if self.queue:
            self.queue.insert(0, num)
        else:
            self.queue.append(num)

    def reverse(self):
        if self.queue:
            self.queue.reverse()


def main():
    queue = Queue()

    queue.add(5)
    queue.add(6)
    print(queue.get_first())
    print(queue.get_first())
    print(queue.get_first())

    queue.add(5)
    queue.add(6)
    print(queue.get_last())
    print(queue.get_last())
    print(queue.get_last())

    # advansed level
    queue.append(5)
    queue.append(6)
    print(queue.get_first())
    print(queue.get_first())

    queue.append(5)
    queue.append(6)
    queue.reverse()
    print(queue.get_first())
    print(queue.get_first())


if __name__ == "__main__":
    main()
