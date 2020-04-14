x = int(input())

for i in range(0, x):
    hora, minuto, acao = input().split(' ')

    if(len(hora) == 1):
        hora = '0' + hora

    if(len(minuto) == 1):
        minuto = '0' + minuto

    time = hora + ':' + minuto

    if(int(acao) > 0):
        print('{} - A porta abriu!'.format(time))
    else:
        print('{} - A porta fechou!'.format(time))
