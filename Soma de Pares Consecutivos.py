while True:
    X = int(input())
    soma = 0
    if X == 0:
        break
    if X % 2 == 0:
        for i in range (5):
            soma += X
            X += 2
    else:
        X += 1
        for i in range (5):
            soma += X
            X += 2
    print(soma)

