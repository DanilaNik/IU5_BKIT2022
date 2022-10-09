def print_result(func):
    def wrapper(lst=[], *args, **kwargs):
        print(func.__name__)

        if len(lst) == 0:
            result = func(*args, **kwargs)
        else:
            result = func(lst, *args, **kwargs)

        if type(result) is dict:
            for key, el in result.items():
                print(f'{key} = {el}')

        elif type(result) is list:
            print('\n'.join(map(str, result)))

        else:
            print(result)

        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main():
    '''
        Необходимо реализовать декоратор print_result, который 
    выводит на экран результат выполнения функции.
        Декоратор должен принимать на вход функцию, вызывать её, 
    печатать в консоль имя функции и результат выполнения, после 
    чего возвращать результат выполнения.
        Если функция вернула список (list), то значения элементов 
    списка должны выводиться в столбик.
        Если функция вернула словарь (dict), то ключи и значения 
    должны выводить в столбик через знак равенства.
    '''
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()