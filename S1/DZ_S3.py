def T16():
    # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

    # *Пример:*

    # 5
    #     1 2 3 4 5
    #     3
    #     -> 1
    n = int(input("Количество элементов в массиве: "))
    input_str = input("Введите " + str(n) + " натуральных чисел через пробел: ")
    input_arr = input_str.split()

    print("Первый ввод:")

    print(n)
    print(input_str)
    print(input_arr)
    print(len(input_arr))

    if len(input_arr) != n: input("Ошибка! Количество введённых элементов: " + str(len(input_arr)) + ". Необходимо " + str(n))

    cnt_occurrences = 0
    for x in input_arr:
        if n == int(x): cnt_occurrences += 1

    print(cnt_occurrences)

# T16()
