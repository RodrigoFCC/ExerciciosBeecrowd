N = int(input())
fatorial = N

for i in range(1,N):
    fatorial *= N-i
print(fatorial)