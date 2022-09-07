N = int(input())

inicial = 1
for i in range(N):
    lista = []

    for item in range(3):
        valor = inicial ** (item+1)
        lista.append(valor)

    print(*lista)
    lista[1] += 1
    lista[2] += 1
    print(*lista)
    inicial += 1