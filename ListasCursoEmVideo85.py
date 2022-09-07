
todos = [[],[]]

for i in range(7):
    valor = int(input('Digite o %do. valor: ' % (i+1)))
    if valor % 2 == 0:
        todos[1].append(valor)
    else:
        todos[0].append(valor)
todos[0].sort()
todos[1].sort()

print('Os valores pares digitados foram: %s' % todos[1])
print('Os valores impares digitados foram: %s' %todos[0])


