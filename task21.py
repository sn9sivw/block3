# Перебор всех возможных значений A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Выражение
            expr_a = not (A or (not B and C))
            # Выражение b
            expr_b = A and not ((B and C) or (not C))
            # Выражение c
            expr_c = not ((not A) or (B and C))
            print(f"A={A}, B={B}, C={C}:")
            print(f"  a) {expr_a}")
            print(f"  b) {expr_b}")
            print(f"  c) {expr_c}")
