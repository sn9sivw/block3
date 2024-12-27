# Определение функций для логических операций
def not_(x):
    return not x


def and_(x, y):
    return x and y


def or_(x, y):
    return x or y


for X in [False, True]:
    for Y in [False, True]:
        expr_a = or_(not_(or_(not_(X), Y)), not_(X))
        expr_b = and_(not_(and_(not_(X), not_(Y))), X)
        expr_c = or_(not_(or_(X, not_(Y))), not_(Y))
        print(f'X={X}, Y={Y}')
        print(f'\ta {expr_a}')
        print(f'\tb) {expr_b}')
        print(f'\tc) {expr_c}')
