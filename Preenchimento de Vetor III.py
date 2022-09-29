X = float(input())
N =[X]
metade = 0
for i in range(99):
    metade = N[i]/2
    N.append(metade)

for x in range(len(N)):
    print(f'N[{x}] = {N[x]:.4f}')