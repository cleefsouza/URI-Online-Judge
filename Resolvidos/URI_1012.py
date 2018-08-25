class areas1012:
    linha = input().split(" ")
    A, B, C = linha
    
    tretangulo = (float(A)*float(C))/2
    circulo = (pow(float(C),2)*3.14159)
    trapezio = ((float(A)+float(B))*float(C))/2
    quadrado = pow(float(B),2)
    retangulo = float(A)*float(B)
    
    print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(tretangulo,circulo,trapezio,quadrado,retangulo))
