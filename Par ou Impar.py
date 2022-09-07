N = int(input())
par = 'EVEN'
impar ='ODD'
positivo = 'POSITIVE'
negativo = 'NEGATIVE'
nulo = 'NULL'

for i in range(N):
    X = int(input())
    if X > 0 and X%2 == 0:
        print(par, positivo)
    elif X > 0 and X%2 != 0:
        print(impar, positivo)
    elif X < 0 and X%2 == 0:
        print(par, negativo)
    elif X < 0 and X%2 != 0:
        print(impar, negativo)
    elif X == 0:
        print(nulo)



