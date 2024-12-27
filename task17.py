num = [(True, True), (True, False), (False, True), (False, False)]


def compute_expressions(A, B):
    a = (not A and not B) or A
    b = B or (not A and not B)
    c = B and not (A and not B)
    return a, b, c


for A, B in num:
    a, b, c = compute_expressions(A, B)
    print(f"А={A}, B={B}:")
    print(f"\ta) не А и не В или А = {a}")
    print(f"\tb) В или не А и не В = {b}")
    print(f"\tv) В и не (А и не В) = {c}")
    print()
