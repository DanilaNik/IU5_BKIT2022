from random import randint

def gen_random(count_num, begin, end):
    rand_arr = []
    for i in range(count_num):
        rand_arr.append(randint(begin,end))
    return rand_arr

def main():
    '''
        Необходимо реализовать генератор gen_random(количество, минимум, максимум),
    который последовательно выдает заданное количество случайных 
    чиселв заданном диапазоне от минимума до максимума, включая 
    границы диапазона. 
    Пример:
    gen_random(5, 1, 3) должен выдать 5 случайных чисел в диапазоне 
    от 1 до 3, например 2, 2, 3, 2, 1
    '''
    numbers = gen_random(5, 1, 3)
    for i in numbers:
        print(numbers[i], end = ' ')
    print()

if __name__ == '__main__':
    main()
