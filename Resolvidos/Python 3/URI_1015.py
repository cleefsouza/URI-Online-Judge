import math

class distancia2pontos1015:
    p1 = input().split(" ")
    p2 = input().split(" ")
    
    x1, y1 = p1
    x2, y2 = p2
    
    calculo = (((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2))
    raiz = math.sqrt(calculo)
    
    print('{:.4f}'.format(raiz))
