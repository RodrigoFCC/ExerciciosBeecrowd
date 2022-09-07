X = int(input())
Y = int(input())

if X > Y:
    maior = X
    menor = Y
else:
    maior = Y
    menor = X
soma = 0
for i in range(menor,maior+1):
    if i % 13 != 0:
        soma += i

print(soma)