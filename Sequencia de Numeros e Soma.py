M = 1
N = 1

while M > 0 and N > 0:
    M,N = input().split()

    M = int(M)
    N = int(N)
    if M > 0 and N > 0:
        lista = []
        soma = 0
        if M > N:
            maior = M
            menor = N
        else:
            maior = N
            menor = M
        for i in range(menor,maior+1):
            lista.append(i)
            soma += i
        print (*lista,'Sum=%d' % soma)

