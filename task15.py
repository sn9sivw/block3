num = [(True, True), (True, False), (False, True), (False, False)]


def compute_expressions(A, B):
    a = not A or not B
    b = A and (A or not B)
    c = (not A or B) and B
    return a, b, c


for A, B in num:
    a, b, c = compute_expressions(A, B)
    print(f"А={A}, B={B}:")
    print(f"\n) не А или не В = {a}")
    print(f"\n) А и (А или не В) = {b}")
    print(f"\n) (не А или В) и В = {c}")
    print()
