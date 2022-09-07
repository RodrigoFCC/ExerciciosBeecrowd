matriz = []

for i in range(3):
    lista = []
    for j in range(3):
        numero = int(input())
        lista.append(numero)
    matriz.append(lista)
for i in range(3):
    for j in range(3):
        print('[  %s  ]' % matriz[i][j], end = " ")
    print()





