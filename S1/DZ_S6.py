# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
def arithmetic_progres_ar(a1, d, n):
    return [a1 + (i - 1) * d for i in range(1, n + 1)]

def T30():
    a1 = int(input("Введите первый элемент: "))
    d = int(input("Введите разность: "))
    n = int(input("Введите количество элементов: "))
    
    print(arithmetic_progres_ar(a1, d, n))

# T30()

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
def find_ind_el_belong_range(input_ar, minmin, maxmax):
    return [i for i in range(len(input_ar)) if input_ar[i] >= minmin and input_ar[i] <= maxmax]

from random import randint
def T32():
    # input_str = input("Введите массив: ")
    # input_ar = [int (x) for x in input_str.split()]

    n = int(input("Введите количество элементов в массиве: "))
    input_ar = []
    for _ in range(n):
        input_ar.append(randint(-50, 51))

    minmin = int(input("Введите минимум диапозона: "))
    maxmax = int(input("Введите максимум диапозона: "))

    print(input_ar)

    print(find_ind_el_belong_range(input_ar, minmin, maxmax))

T32()
