N = 1

while N != 0:
    lista = []
    N = int(input())
    if N > 0:
        for i in range(N):
            valor = i + 1
            lista.append(valor)
        print(*lista)
    if N == 0:
        X = 0


