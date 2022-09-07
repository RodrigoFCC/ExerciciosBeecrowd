X,Y = input().split()

X = int(X)
Y = int(Y)
p = 0

while p < Y:
    lista = []
    for i in range(X):
        p += 1
        lista.append(p)
    print(*lista)