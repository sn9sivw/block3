def threatens_rook(a, b, c, d):
    return a == c or b == d


def threatens_bishop(a, b, c, d):
    return abs(a - c) == abs(b - d)


def threatens_king(a, b, c, d):
    return abs(a - c) <= 1 and abs(b - d) <= 1


def threatens_queen(a, b, c, d):
    return threatens_rook(a, b, c, d) or threatens_bishop(a, b, c, d)


def can_move_white_pawn_normal(a, b, c, d):
    return a == c and b + 1 == d


def can_capture_white_pawn(a, b, c, d):
    return abs(a - c) == 1 and b + 1 == d


def can_move_black_pawn_normal(a, b, c, d):
    return a == c and b - 1 == d


def can_capture_black_pawn(a, b, c, d):
    return abs(a - c) == 1 and b - 1 == d


if __name__ == "__main__":
    a, b, c, d = 4, 5, 6, 7
    if threatens_rook(a, b, c, d):
        print("Ладья угрожает полю")

    if threatens_bishop(a, b, c, d):
        print("Слон угрожает полю")

    if threatens_king(a, b, c, d):
        print("Король угрожает полю")

    if threatens_queen(a, b, c, d):
        print("Ферзь угрожает полю")

    if can_move_white_pawn_normal(a, b, c, d):
        print("Белая пешка может сделать обычный ход на это поле")

    if can_capture_white_pawn(a, b, c, d):
        print("Белая пешка может побить фигуру на этом поле")

    if can_move_black_pawn_normal(a, b, c, d):
        print("Черная пешка может сделать обычный ход на это поле")

    if can_capture_black_pawn(a, b, c, d):
        print("Черная пешка может побить фигуру на этом поле")
