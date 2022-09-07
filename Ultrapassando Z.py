X = int(input())
Z = int(input())
soma = 0
contagem = 0
while X >= Z:
    Z = int(input())

while soma <= Z:
    soma += X
    contagem += 1
    X += 1

print(contagem)