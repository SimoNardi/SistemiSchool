"""da implementare: i grafi pesati, il networkx"""

def main():
    print(user2adj())


def user2adj():
    num = int(input("inserire il numero di nodi: "))
    matrice = []
    for i in range(0, num):
        vicine = [int(n) for n in input(f"Inserisci i nodi adiacenti a {i+1}: ").split(",")]
        colonna = [0 for n in range(0, num)]
        for n in vicine:
            if (n != -1):
                colonna[n-1] = 1
        matrice.append(colonna)
    return matrice


def adj2dict():
    pass


if __name__ == '__main__':
    main()