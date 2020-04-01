jogadas = int(input())
for i in range(0, jogadas, 1):
    jog1 = str(input().lower())
    jog2 = str(input().lower())

    if(jog1 == 'ataque' and jog2 == 'ataque'):
        print('Aniquilacao mutua')
    elif(jog1 == 'pedra' and jog2 == 'pedra'):
        print('Sem ganhador')
    elif(jog1 == 'papel' and jog2 == 'papel'):
        print('Ambos venceram')
    elif((jog1 == 'ataque' and (jog2 == 'papel' or jog2 == 'pedra'))
        or (jog1 == 'pedra' and jog2 == 'papel')):
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
