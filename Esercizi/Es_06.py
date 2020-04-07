def readData():
    data = open('data.txt', 'r')
    dictCont = {}

    c = 0
    lines = data.readlines()
    for _, line in lines:
        matrix = []
        matrix.append(lines)
        dictCont[c] = matrix
        c = c + 1
    data.close()

    return dictCont


def toMat(dic):
    matrix = []

    for _, n in dic.items():
        matrix.append(n)
    print(matrix)


def paziente0(mat):
    p0 = []

    for n in range(0, len(mat)):
        trop = 0
        port = 0
        for p in range(0, len(mat)):
            if mat[n][p] != 0:
                port = 1
        if (port == 1):
            k = 0
            while (k < len(mat) and trop == 0):
                if mat[k][n] == 0:
                    k = k + 1
                else:
                    trop = 1
            if trop == 0:
                p0.append(n)
        i = i + 1

    return p0


def main():
    d = readData
    mat = toMat(d)
    p0 = paziente0(mat)
    print(f"i/il paziente/i è/sono {p0}")


if __name__ == "main":
    main()