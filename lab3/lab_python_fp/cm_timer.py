from time import sleep, time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.__time_begin = time()
        # return self.__start

    def __exit__(self, type, value, traceback):
        print(f'Time of work: {time()- self.__time_begin}')


@contextmanager
def cm_timer_2():
    time_begin = time()
    yield 
    print(f'Time of work: {time() - time_begin}')


def main():
    with cm_timer_1():
       sleep(2.0)

    with cm_timer_2():
        sleep(2.0)

if __name__ == '__main__':
    main()