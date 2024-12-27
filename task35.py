def threatens_rook(c, d, e, f):
    return c == e or d == f


def threatens_queen(c, d, e, f):
    return c == e or d == f or abs(c - e) == abs(d - f)


def threatens_knight(c, d, e, f):
    return ((abs(e - c) == 2 and abs(f - d) == 1) or
            (abs(e - c) == 1 and abs(f - d) == 2))


def threatens_bishop(c, d, e, f):
    return abs(c - e) == abs(d - f)


def threatens_king(c, d, e, f):
    return abs(c - e) <= 1 and abs(d - f) <= 1


def can_move_and_safe(white_piece, black_piece, a, b, c, d, e, f):

    if white_piece == 'rook':
        if not threatens_rook(c, d, e, f):
            return True
    elif white_piece == 'queen':
        if not threatens_queen(c, d, e, f):
            return True
    elif white_piece == 'knight':
        if not threatens_knight(c, d, e, f):
            return True
    elif white_piece == 'bishop':
        if not threatens_bishop(c, d, e, f):
            return True
    elif white_piece == 'king':
        if not threatens_king(c, d, e, f):
            return True
    else:
        raise ValueError('Неправильный тип белой фигуры')
    return False


if __name__ == "__main__":
    a, b, c, d, e, f = 1, 1, 2, 2, 3, 3
    result = can_move_and_safe('rook', 'rook', a, b, c, d, e, f)
    print(f'Ладья и ладья: {result}')

    result = can_move_and_safe('rook', 'queen', a, b, c, d, e, f)
    print(f'Ладья и ферзь: {result}')

    result = can_move_and_safe('rook', 'knight', a, b, c, d, e, f)
    print(f'Ладья и конь: {result}')

    result = can_move_and_safe('rook', 'bishop', a, b, c, d, e, f)
    print(f'Ладья и слон: {result}')

    result = can_move_and_safe('queen', 'queen', a, b, c, d, e, f)
    print(f'Ферзь и ферзь: {result}')

    result = can_move_and_safe('queen', 'rook', a, b, c, d, e, f)
    print(f'Ферзь и ладья: {result}')

    result = can_move_and_safe('queen', 'knight', a, b, c, d, e, f)
    print(f'Ферзь и конь: {result}')

    result = can_move_and_safe('queen', 'bishop', a, b, c, d, e, f)
    print(f'Ферзь и слон: {result}')

    result = can_move_and_safe('knight', 'knight', a, b, c, d, e, f)
    print(f'Конь и конь: {result}')

    result = can_move_and_safe('knight', 'rook', a, b, c, d, e, f)
    print(f'Конь и ладья: {result}')

    result = can_move_and_safe('knight', 'queen', a, b, c, d, e, f)
    print(f'Конь и ферзь: {result}')

    result = can_move_and_safe('knight', 'bishop', a, b, c, d, e, f)
    print(f'Конь и слон: {result}')

    result = can_move_and_safe('bishop', 'bishop', a, b, c, d, e, f)
    print(f'Слон и слон: {result}')

    result = can_move_and_safe('bishop', 'queen', a, b, c, d, e, f)
    print(f'Слон и ферзь: {result}')

    result = can_move_and_safe('bishop', 'knight', a, b, c, d, e, f)
    print(f'Слон и конь: {result}')

    result = can_move_and_safe('bishop', 'rook', a, b, c, d, e, f)
    print(f'Слон и ладья: {result}')

    result = can_move_and_safe('king', 'bishop', a, b, c, d, e, f)
    print(f'Король и слон: {result}')

    result = can_move_and_safe('king', 'queen', a, b, c, d, e, f)
    print(f'Король и ферзь: {result}')

    result = can_move_and_safe('king', 'knight', a, b, c, d, e, f)
    print(f'Король и конь: {result}')

    result = can_move_and_safe('king', 'rook', a, b, c, d, e, f)
    print(f'Король и ладья: {result}')
