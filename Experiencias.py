N = int(input())
coelhos = 0
ratos = 0
sapos = 0
total = 0

for i in range(N):
    quantidade,tipo = input().split()
    quantidade = int(quantidade)
    total += quantidade
    if tipo == 'C':
        coelhos += quantidade

    elif tipo == 'R':
        ratos += quantidade

    elif tipo == 'S':
        sapos += quantidade

porcentagemC = (coelhos*100)/ total
porcentagemR = (ratos*100)/ total
porcentagemS = (sapos*100)/ total

print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % coelhos)
print('Total de ratos: %d' % ratos)
print('Total de sapos: %d' % sapos)
print('Percentual de coelhos: %.2f %%' % porcentagemC)
print('Percentual de ratos: %.2f %%' % porcentagemR)
print('Percentual de sapos: %.2f %%' % porcentagemS)