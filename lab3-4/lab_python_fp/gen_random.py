from random import randint

def gen_random(count_num, begin, end):
    rand_arr = []
    for i in range(count_num):
        rand_arr.append(randint(begin,end))
    return rand_arr

def main():
    numbers = gen_random(5, 1, 3)
    for i in numbers:
        print(numbers[i], end = ' ')
    print()

if __name__ == '__main__':
    main()
