entrada = 0
alcool = 0
gasolina= 0
diesel = 0

while entrada != 4:
    combustivel = int(input())
    if combustivel == 1:
        alcool += 1
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1
    elif combustivel == 4:
        entrada = 4

print('MUITO OBRIGADO')
print('Alcool: %d' % alcool)
print('Gasolina: %d' % gasolina)
print('Diesel: %d' % diesel)

