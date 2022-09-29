A = []
for i in range(5):
    numero = float(input())
    A.append(numero)
for i in range(len(A)):
    if A[i] == 10 or A[i]<= 0:
        print(f'A[{i}] = {A[i]:.1f}')