T = int(input())
N =[]
while len(N) < 1000:
    for i in range(T):
        if len(N) < 1000:
            N.append(i)

for x in range(len(N)):
    print(f'N[{x}] = {N[x]}')