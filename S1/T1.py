# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input("Сколько проезжает в день: "))
m = int(input("Сколько нужно проехать: "))
ostatok = int(bool(m % n))
days = m // n + ostatok
print(days)