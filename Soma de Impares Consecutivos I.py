X = int(input())
Y = int(input())

if X > Y:
    valormaior = X
    valormenor = Y
else:
    valormaior = Y
    valormenor = X

if valormenor%2 == 0:
    valormenor += 1
else:
    valormenor += 2

soma = 0
for i in range(valormenor,valormaior,2):
    soma += i

print(soma)