M = []
L = int(input())
T = input()
soma = 0
media = 0
for i in range(12):
    lista = []
    M.append(lista)
    for j in range(12):
        if L == i:
            valor = float(input())
            lista.append(valor)
            soma += valor
        else:
            valor = float(input())
            lista.append(valor)

media = soma/12
if T == 'S':
    print(soma)
elif T == 'M':
    print(f'{media:.1f}')