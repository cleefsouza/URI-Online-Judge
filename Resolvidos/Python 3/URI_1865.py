class mjolnir:
    
    c = int(input())
    while(c!=0):
        linha = input().split(" ")
        
        nome = str(linha[0])
        n = int(linha[1])
        
        if(n>=1 and n<=25000):
            if(nome=="Thor"):
                print('Y')
            else:
                print('N')
            
            c-=1
