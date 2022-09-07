X = int(input())
Y = int(input())

if X > Y:
    maior = X
    menor = Y
else:
    maior = Y
    menor = X
soma = 0
for i in range(menor+1,maior):
    if i % 5 == 2 or i % 5 == 3:
        print(i)