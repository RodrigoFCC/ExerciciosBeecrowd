N = []
numero = int(input())
N.append(numero)
for i in range(9):
    numero *= 2
    N.append(numero)
for i in range(len(N)):
    print(f'N[{i}] = {N[i]}')