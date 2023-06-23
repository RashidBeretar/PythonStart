# Задача №11. Общее обсуждение
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# 1 1 2 3 5 8 13
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,

a = int(input("Введите A: "))

0 - 1
1 - 2, 3
2 - 4
3 - 5
4 - -1
5 - 6

# 
# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)
# /

if a == 0: n = 1
elif a == 1: n = "1, 2"
else:
    number_last_last = 0
    number_last = 0
    number_cur = 0
    n = 0
    while number_cur < a:
        # print(n)
        if n == 1: number_cur = 1
        else: number_cur = number_last + number_last_last
        number_last_last = number_last
        number_last = number_cur
        n += 1
    if number_cur != a: n = -1

print("Ответ:", n)