class consumo1014:
    distancia = int(input())
    litros = float(input())
    
    media = float(distancia/litros)
    
    print('{:.3f} km/l'.format(media))
