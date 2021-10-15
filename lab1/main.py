import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        coef_str = sys.argv[index]
    except IndexError: pass

    while True:
        try:
            coef = float(coef_str)
            break
        except (UnboundLocalError, ValueError) as e: pass

        print(prompt)
        coef_str = input()

    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    roots = []
    D = b * b - 4 * a * c
    signs = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

    for sign1, sign2 in signs:
        try:
            sqD = math.sqrt(D)
            roots.append(sign2 * math.sqrt((-b + sign1 * sqD) / (2.0 * a)))
        except ZeroDivisionError:
            try:
                roots.append(sign1 * math.sqrt(-c/b))
            except: pass
        except ValueError: pass
    
    if a == b == c == 0:
        roots = ['любое число']
    
    if len(roots) == 0:
        roots = ['нет корней']

    return set(roots)


def print_root(root):
    print(str(root), end=' ')


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    # Вычисление корней
    roots = get_roots(a,b,c)

    # Вывод корней
    print('Корни:', end=' ')
    [print_root(root) for root in roots]


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
