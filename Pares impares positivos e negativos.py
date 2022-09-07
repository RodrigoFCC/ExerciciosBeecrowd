pares = 0
impares = 0
positivos = 0
negativos =0

for i in range(5):
    valor = int(input())
    if valor%2 == 0:
        pares += 1
    else:
        impares += 1
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print('%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativos(s)' % (pares,impares,positivos,negativos))