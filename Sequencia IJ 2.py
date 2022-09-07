I = 1
J = 8
for x in range(5):
    for i in range (3):
        J -= 1
        print('I=%d J=%d' % (I,J))
    I += 2
    J = 8