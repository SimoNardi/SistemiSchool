grid = [[True, True, True, True, True, False],
        [False, False, True, True, True, False],
        [True, True, True, False, True, True],
        [True, False, False, True, True, False],
        [True, True, True, True, False, True],
        [True, False, True, True, True, False]]


def matrix2dict(matrix):
    counter = 1
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            if matrix[x][y]:
                matrix[x][y] = counter
                counter = counter + 1

    for row in matrix:
        print(row)

    dict = {}
    x = 1  # spostamento dx, sx, su, giù
    nNodi = 1
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix)):
            links = []
            if matrix[r][c] != False:
                if r - x >= 0:
                    if (matrix[r - x][c] != False): links.append(matrix[r - x][c])
                if c - x >= 0:
                    if (matrix[r][c - x] != False): links.append(matrix[r][c - x])
                if c + x < len(matrix):
                    if (matrix[r][c + x] != False): links.append(matrix[r][c + x])
                if r + x < len(matrix):
                    if (matrix[r + x][c] != False): links.append(matrix[r + x][c])
                dict[nNodi] = links
                nNodi += 1
    return dict


print(matrix2dict(grid))