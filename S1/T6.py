# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input("Введите шестизначное число: "))
# number = 385916

f_data_validation = True

number_cnt = len(str(number))
if number_cnt % 2 != 0 or number_cnt < 2: f_data_validation = False

part1 = 0
part2 = 0
i = 1
if f_data_validation:
    half = number_cnt // 2
    
    while number > 0:
        if i > half:
            part1 += number % 10
        else:
            part2 += number % 10
        number //= 10
        i += 1

    # print(half, part1, part2)
    print("yes" if part1 == part2 else "no")
else:
    print("Ошибка! Введите корректное число")