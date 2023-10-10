# "П - профилирование
# Сегодня мы напишем довольно полезный класс, который поможет нам замерять время работы наших программ и отдельных частей.
# Суть задачи максимально простая — надо написать удобный в использовании класс, с помощью которого можно замерить работу какого-то
# участка кода. Вот самый простой пример подобного кода (не оформленного в виде класса), который можно взять за основу:
# start_time = getCurrentTime();
# callMethod();
# run_time = getCurrentTime() - start_time;
# print(""callMethod() worked "" + run_time "" seconds"");
# Здесь мы замеряем время работы метода callMethod в секундах. От класса ожидается возможность замеры времени в секундах (полезно для UI тестов)
# и миллисекундах (полезно для API и unit тестов)."

import time


class Timing:

    def __init__(self, function=None):
        self.func = function
        self.start_time = None
        self.stop_time = None

    def start(self):
        self.start_time = time.time()
        return self

    def stop(self):
        self.stop_time = time.time()
        return self

    def function(self, function):
        self.start_time = time.time()
        self.func = function
        return self

    def in_second(self):
        if self.func:
            self.func()
        self.stop_time = time.time()
        return round(self.stop_time - self.start_time, 1)

    def in_millisecond(self):
        return round(self.in_second() * 1000,  1)


def function_by_test():
    time.sleep(1)


if __name__ == '__main__':
    timer = Timing()

    print(timer.function(function_by_test).in_second())

    timer.start()
    time.sleep(1.5)
    print(timer.stop().in_millisecond())
