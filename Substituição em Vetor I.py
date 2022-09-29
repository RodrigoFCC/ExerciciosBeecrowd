X = []
for i in range(10):
    numero = int(input())
    if numero < 0 or numero == 0:
        numero = 1
    X.append(numero)
for i in range(len(X)):
    print(f'X[{i}] = {X[i]}')

