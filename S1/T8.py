# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))

print("n = ", n, ", m = ", m, ", k = ", k)
print("yes" if k < n * m and ((k % n == 0 and k >= n) or (k % m == 0 and k >= m)) else "no")