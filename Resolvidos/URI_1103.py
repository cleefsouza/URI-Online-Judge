class alarmedespertador:
    while True:
        linha = input().split(" ")
        
        h1 = int(linha[0])
        m1 = int(linha[1])
        h2 = int(linha[2])
        m2 = int(linha[3])
        
        if(h1==0 and m1==0 and h2==0 and m2==0):
            break
        if(h1>=0 and h1<=23 and m1>=0 and m1<=59 and h2>=0 and h2<=23 and m2>=0 and m2<=59):
            t1 = (h1 * 60)+m1
            t2 = (h2 * 60)+m2
        
        if(t1<t2):
            print(t2-t1)
        else:
            print(1440+(t2-t1))
