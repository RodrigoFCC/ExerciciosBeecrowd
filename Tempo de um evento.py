diaInicial = int(input().split()[1])
hora = input().split(':')
horaInicial = int(hora[0])
minutoInicial = int(hora[1])
segundoInicial = int(hora[2])

diaFinal = int(input().split()[1])
hora = input().split(':')
horaFinal = int(hora[0])
minutoFinal = int(hora[1])
segundoFinal = int(hora[2])


dias = diaFinal - diaInicial
horas =  horaFinal - horaInicial

if horas < 0:
    horas += 24
    dias -= 1

minutos = minutoFinal - minutoInicial
segundos = segundoFinal - segundoInicial

if segundos < 0:
    segundos += 60
    minutos -= 1

if minutos < 0:
    minutos += 60
    horas -= 1

print('%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)' % (dias, horas, minutos, segundos))