N = int(input())
somaIn = 0
somaOut = 0
for i in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        somaIn += 1
    else:
        somaOut += 1
print('%d in\n%d out' % (somaIn,somaOut))
