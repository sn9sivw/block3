# Определение функций для логических операций
def not_(x):
    return not x


def and_(x, y):
    return x and y


def or_(x, y):
    return x or y


# Таблица истинности для каждой комбинации A и B
for A in [False, True]:
    for B in [False, True]:
        # Логическое выражение a)
        expr_a = and_(not_(and_(not_(A), not_(B))), A)

        # Логическое выражение b)
        expr_b = or_(not_(or_(not_(A), not_(B))), A)

        # Логическое выражение c)
        expr_c = and_(not_(or_(not_(A), not_(B))), B)

        print(f'A={A}, B={B}:')
        print(f'\ta) {expr_a}')
        print(f'\tb) {expr_b}')
        print(f'\tc) {expr_c}')
