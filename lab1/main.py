import sys
import math


def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    flag = False
    # Проверка на число
    while (flag == False):
        try:
            # Пробуем перевести строку в действительное число
            coef = float(coef_str)
        except:
            # При ошибке просим повторить ввод коэффициента
            print(prompt)
            coef_str = input()
        else:
            flag = True
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        quadratic1 = (-b + sqD) / (2.0 * a)
        quadratic2 = (-b - sqD) / (2.0 * a)
        # y = x^2 проверяем игрек на положительность
        if (quadratic1 >= 0):
            root1 = math.sqrt(quadratic1)
            root2 = -root1
            result.append(root1)
            if (root1 != root2):
                result.append(root2)
        if (quadratic2 >= 0):
            root3 = math.sqrt(quadratic2)
            root4 = -root3
            result.append(root3)
            if (root3 != root4):
                result.append(root4)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Действительных корней нет')
    elif len_roots == 1:
        print(f'Один корень: {roots[0]}')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    else:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2],
                                                       roots[3]))


if __name__ == "__main__":
    main()