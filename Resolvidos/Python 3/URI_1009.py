class salariobonus1009:
    nome = str(input())
    salariofixo = float(input())
    vendas = float(input())
    
    comissao = float((0.15*vendas)+salariofixo)
    
    print('TOTAL = R$ {:.2f}'.format(comissao))
