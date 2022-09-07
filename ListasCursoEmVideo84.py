continuar = 's'
nomes = []
pesos = []
while continuar == 's':
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    nomes.append(nome)
    pesos.append(peso)
    continuar = input('Quer continuar? [S/N] ')
print('-=' * 20)
print('Ao todo, você cadastrou %d pessoas' % len(nomes))
maior = 0
menor = 1000
listaMaior = []
listaMenor = []

for i in range(len(pesos)):
    if pesos[i] > maior:
        maior = pesos[i]
    if pesos[i] < menor:
        menor = pesos[i]
for i in range(len(pesos)):
    if maior == pesos[i]:
         listaMaior.append(nomes[i])
    elif menor == pesos[i]:
        listaMenor.append(nomes[i])

print('O maior peso foi de %.1f. Peso de %s' % (maior,listaMaior))
print('O menor peso foi de %.1f. Peso de %s' % (menor,listaMenor))






