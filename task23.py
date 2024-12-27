# Функция для вывода результата
def calculate_and_print(A, B, C):
    expr_a = not (A or (not B and C)) or C
    expr_b = not (A and (not B or C)) and B
    expr_c = not ((not A) or (B and C)) or A
    print(f'A={A}, B={B}, C={C}')
    print(f'a) {expr_a}')
    print(f'b) {expr_b}')
    print(f'c) {expr_c}')
    print()


# Перебор всех возможных значений A, B и C
for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            calculate_and_print(A, B, C)
