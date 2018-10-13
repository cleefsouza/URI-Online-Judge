class combustivel1017:
    hora = int(input())
    dist = int(input())
    
    litr = (dist*hora)/12
    
    print('{:.3f}'.format(litr))
