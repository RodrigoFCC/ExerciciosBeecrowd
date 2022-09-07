idade = 1
lista = []
soma = 0
while idade > 0:
    idade = int(input())
    if idade > 0:
        soma += idade
        lista.append(idade)
media = soma/len(lista)
print('%.2f' % media)

