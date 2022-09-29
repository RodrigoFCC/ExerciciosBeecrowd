par = []
impar = []

for i in range(15):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    if len(par) == 5:
        for x in range(len(par)):
            print(f'par[{x}] = {par[x]}')
        par = []
    elif len(impar) == 5:
        for x in range(len(impar)):
            print(f'impar[{x}] = {impar[x]}')
        impar = []

for x in range(len(impar)):
    print(f'impar[{x}] = {impar[x]}')
for x in range(len(par)):
    print(f'par[{x}] = {par[x]}')