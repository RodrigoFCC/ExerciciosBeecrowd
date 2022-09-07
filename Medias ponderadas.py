N = int(input())

for i in range(N):
  valor = input().split()
  media = (float(valor[0])*2 + float(valor[1])*3+ float(valor[2])*5)/ 10
  print('%.1f' % media)