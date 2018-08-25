class salario1008:
    numfunc = int(input())
    horatrab = int(input())
    valorhr = float(input())
    
    salario = float(valorhr*horatrab)
    
    print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(numfunc,salario))
