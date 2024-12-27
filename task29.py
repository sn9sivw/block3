X = int(input("Введите число X: "))
Y = int(input("Введите число Y: "))
Z = int(input("Введите число Z: "))

condition_a = (X % 2 == 1) and (Y % 2 == 1)
condition_b = (X < 20) ^ (Y < 20)
condition_v = (X == 0) or (Y == 0)
condition_g = (X < 0) and (Y < 0) and (Z < 0)
condition_d = (X % 5 == 0) + (Y % 5 == 0) + (Z % 5 == 0) == 1
condition_e = (X > 100) or (Y > 100) or (Z > 100)

print("Результат:")
print(f"а) Каждое из чисел X и Y нечетное: {condition_a}")
print(f"б) Только одно из чисел X и Y меньше 20: {condition_b}")
print(f"в) Хотя бы одно из чисел X и Y равно нулю: {condition_v}")
print(f"г) Каждое из чисел X, Y, Z отрицательное: {condition_g}")
print(f"д) Только одно из чисел X, Y и Z кратно пяти: {condition_d}")
print(f"е) Хотя бы одно из чисел X, Y, Z больше 100: {condition_e}")
