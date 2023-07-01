# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
def exponentiation_recursive(A, B):
    if B == 0:
        return 1

    if B <= 1:
        return A
    else:
        return A * exponentiation_recursive(A, B - 1)
    
def T26():
    A = int (input("Введите A: "))
    B = int (input("Введите B: "))
    print(A)
    print(B)
    
    print(exponentiation_recursive(A, B))

# T26()

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4  
def sum28(a, b):
    if b <= 0:
        return a
    else:
        return sum28(a, b - 1) + 1

def T28():
    a = int (input("Введите a: "))
    b = int (input("Введите b: "))
    print(a)
    print(b)
    
    print(sum28(a, b))

T28()
