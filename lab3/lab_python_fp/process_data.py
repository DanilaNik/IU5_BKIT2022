from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
import json
import sys

try:
    path = sys.argv[1]
    print(path)
except:
    path = 'data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg) -> list:
    return sorted(list(set([el['job-name'] for el in arg])), key=lambda x: x.lower())


@print_result
def f2(arg) -> list:
    return list(filter(lambda text: (text.split())[0].lower() == 'программист', arg))


@print_result
def f3(arg) -> list:
    return list(map(lambda lst: lst + ' с опытом Python', arg))


@print_result
def f4(arg) -> list:
    return list(zip(arg, ['зарплата ' + str(el) + ' руб.' for el in gen_random(len(arg), 100000, 200000)]))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
