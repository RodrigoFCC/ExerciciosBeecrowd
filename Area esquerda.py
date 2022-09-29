M = []
O = input()
soma = 0
media = 0
divisor = 0

margemIniciali = 1
margemFinali = 11
margemInicialj = 0
margemFinalj = 1

for i in range(12):
    lista = []
    M.append(lista)
    for j in range(12):
        valor = float(input())
        lista.append(valor)

for i in range(margemIniciali, margemFinali):
    if i == 10:
        margemFinalj = 1
    if i == 6:
        margemFinalj = 5
    for j in range(margemInicialj, margemFinalj):
        soma += M[i][j]
        divisor += 1

    margemIniciali += 1
    margemFinali -= 1

    if margemFinalj <= 5 and i <= 5:
        margemFinalj += 1
    else:
        margemFinalj -= 1

media = soma / divisor
if O == 'S':
    print(f'{soma:.1f}')
elif O == 'M':
    print(f'{media:.1f}')