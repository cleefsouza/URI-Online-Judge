class menorposicao:
    n = int(input())
    if(n>1 and n<1000):
        x = [int(i) for i in input().split()]
        
        print('Menor valor: {}\nPosicao: {}'.format(min(x), (x.index(min(x)))))
