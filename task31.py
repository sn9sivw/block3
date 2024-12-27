N = int(input("Введите целое число N: "))

condition_a = (N % 5 == 0) or (N % 7 == 0)
condition_b = (N % 4 == 0) and (N % 10 != 0)

print("Результат:")
print(f"а) Целое N кратно пяти или семи: {condition_a}")
print(f"б) Целое N кратно четырём и не оканчивается нулем: {condition_b}")
