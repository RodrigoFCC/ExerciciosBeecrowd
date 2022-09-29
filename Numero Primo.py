N = int(input())
for i in range (N):
    X = int(input())
    soma = 0
    for i in range(1,X+1):
        if X % i == 0:
            soma += i
    if soma == (X+1):
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')