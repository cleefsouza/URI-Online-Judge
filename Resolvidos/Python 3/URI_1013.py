class omaior1013:
    import math
    
    linha = input().split(" ")
    a, b, c = linha
    maior = (int(a)+int(b)+abs(int(a)-int(b)))/2
    resu = (int(maior)+int(c)+abs(int(maior-int(c))))/2
    
    print('{:.0f} eh o maior'.format(resu))
