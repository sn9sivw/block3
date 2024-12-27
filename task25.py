# Перебор всех возможных значений A, B и C
for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            expr_a = not (A and B) and (not A or not C)
            expr_b = not (A and not B) or (A or not C)
            expr_c = A and not B or not (A or not C)
            print(f'A={A}, B={B}, C={C}:')
            print(f'а) {expr_a}')
            print(f'б) {expr_b}')
            print(f'в) {expr_c}')
            print()
