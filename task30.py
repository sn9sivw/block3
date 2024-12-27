A = int(input("Введите целое число A: "))

condition_a = (A % 2 == 0) or (A % 3 == 0)
condition_b = (A % 3 != 0) and (A % 10 == 0)

print("Результат:")
print(f"а) Целое А кратно двум или трем: {condition_a}")
print(f"б) Целое А не кратно трем и оканчивается нулем: {condition_b}")
