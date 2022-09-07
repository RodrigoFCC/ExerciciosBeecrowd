lista =[0,1]
soma = 0
N = int(input())
for i in range(1,N-1):
    soma = lista[i] + lista[i-1]
    lista.append(soma)
print(*lista)


