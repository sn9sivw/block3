def evaluate_expression(x, y, z):
    expression_a = not (x or (not y and z))

    expression_b = y or (x and (not y or z))

    expression_c = not ((not x and y) or z)

    return expression_a, expression_b, expression_c


for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            result_a, result_b, result_c = evaluate_expression(x, y, z)
            print(f'X={x}, Y={y}, Z={z}')
            print(f'а) {result_a}')
            print(f'б) {result_b}')
            print(f'в) {result_c}')
            print()
