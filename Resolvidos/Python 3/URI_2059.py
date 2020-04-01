valores = input().split(' ')

p, j1, j2, r, a = int(valores[0]),  int(valores[1]), int(valores[2]), int(valores[3]), int(valores[4])
par = False
resul = j1 + j2

if(p == 1): par = True

if(r == 1 and a == 1):
    print('Jogador 2 ganha!')
elif((r == 0 and a == 1) or (r == 1 and a == 0)):
    print('Jogador 1 ganha!')
elif((resul % 2 == 0)
    and par == True):
    print('Jogador 1 ganha!')
elif((resul % 2 == 1)
    and par == False):
    print('Jogador 1 ganha!')
else:
    print('Jogador 2 ganha!')
