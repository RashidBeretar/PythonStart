# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
# def T37():
#     n = int (input("Введите натуральное число: "))

n = int (input("Введите натуральное число: "))

    

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
def is_simple(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def T35():
    print(is_simple(int (input("Введите число: "))))

# T35()

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
def avenger(input_arr):
    minmin = min(input_arr)
    maxmax = max(input_arr)
    if minmin != maxmax: 
        input_arr = [minmin if x == maxmax else x for x in input_arr]
    return input_arr

def T33():
    input_str = input("Введите массив: ")
    input_arr = [int (x) for x in input_str.split()]

    print(avenger(input_arr))

# T33()
