T = int(input())

for teste in range(T):
    PA,PB,G1,G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1) / 100
    G2 = float(G2) / 100
    anos = 0
    while PA <= PB:
        PA += int(PA * G1)
        PB += int(PB * G2)
        anos += 1
        if anos > 100:
            break

    if anos <= 100:
        print(anos, 'anos.')
    else:
        print('Mais de 1 seculo.')