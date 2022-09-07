N = int(input())

inicial = 0
for i in range(N):
    lista = []
    for item in range(4):
        inicial += 1
        lista.append(inicial)

    lista[3] = 'PUM'
    print(*lista)
