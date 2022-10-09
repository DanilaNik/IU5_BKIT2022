from gen_random import gen_random
class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self._data = items
        self._ignore_case = ignore_case
        self.__used_data = set()
        self.__index = 0

    def __next__(self):
        # Если игнорируем капс, то пробегаемся по списку и приводим всё к общему капсу.
        if self._ignore_case:
            for counter, el in enumerate(self._data):
                if type(el) is str:
                    self._data[counter] = el.lower()

        while True:
            if self.__index >= len(self._data):
                raise StopIteration
            else:
                current = self._data[self.__index]
                self.__index += 1
                # если текущего числа ещё не было, добавляем и возвращаем.
                if current not in self.__used_data:
                    self.__used_data.add(current)
                    return current

    def __iter__(self):
        return self


def main():
    '''
        Необходимо реализовать итератор Unique(данные), который 
    принимает на вход массив или генератор и итерируется по 
    элементам,пропуская дубликаты.
        Конструктор итератора также принимает на вход именованный 
    bool-параметр ignore_case, в зависимости от значения которого 
    будут считаться одинаковыми строки в разном регистре.По умолчанию этот
    параметр равен False. 
        При реализации необходимо использовать конструкцию **kwargs. 
        Итератор должен поддерживать работу как со списками, так и 
    с генераторами.
        Итератор не должен модифицировать возвращаемые значения.
    '''
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    it = Unique(data, ignore_case=True)
    try:
        while True:
            print(it.__next__())
    except StopIteration:
        print('The error "StopInteration" was caught')
    data = gen_random(10, 1, 3)
    it = Unique(data, ignore_case=True)
    try:
        while True:
            print(it.__next__())
    except StopIteration:
        print('The error "StopInteration" was caught')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    it = Unique(data, ignore_case=True)
    try:
        while True:
            print(it.__next__())
    except StopIteration:
        print('The error "StopInteration" was caught')


if __name__ == '__main__':
    main()