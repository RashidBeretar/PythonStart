# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

count_coin = int(input("Введите количество монет: "))

result = 0
for i in range(count_coin):
    t = int(input("Введите 1, если герб, 0, если решка: "))
    if t == 0: result += 1

print("Ответ:", result)