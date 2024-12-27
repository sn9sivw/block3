# Перебор всех возможных значений X, Y и Z
for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            expr_a = not (Y or (not X and Z)) or Z
            expr_b = X and not (not Y or Z) or Y
            expr_c = not (X or (Y and Z)) or not X
            print(f'X={X}, Y={Y}, Z={Z}:')
            print(f'а) {expr_a}')
            print(f'б) {expr_b}')
            print(f'в) {expr_c}')
            print()
