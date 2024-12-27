# Перебор всех возможных значений X, Y и Z
for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            expr_a = not (X or Y) and (not X or not Z)
            expr_b = not (not X and Y) or (X and not Z)
            expr_c = X or (not Y and not (X or not Z))
            print(f'X={X}, Y={Y}, Z={Z}:')
            print(f'а) {expr_a}')
            print(f'б) {expr_b}')
            print(f'в) {expr_c}')
            print()
