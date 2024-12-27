A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

condition_a = (A > 100) and (B > 100)
condition_b = (A % 2 == 0) != (B % 2 == 0)
condition_v = (A > 0) or (B > 0)
condition_g = (A % 3 == 0) and (B % 3 == 0) and (C % 3 == 0)
condition_d = (A < 50) + (B < 50) + (C < 50) == 1
condition_e = (A < 0) or (B < 0) or (C < 0)

print("Результат:")
print(f"а) Каждое из чисел А и В больше 100: {condition_a}")
print(f"б) Только одно из чисел А и В чётное: {condition_b}")
print(f"в) Хотя бы одно из чисел А и В положительно: {condition_v}")
print(f"г) Каждое из чисел А, В, С кратно трём: {condition_g}")
print(f"д) Только одно из чисел А, В и С меньше 50: {condition_d}")
print(f"е) Хотя бы одно из чисел А, В, С отрицательно: {condition_e}")
