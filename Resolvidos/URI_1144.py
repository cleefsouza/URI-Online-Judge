class sequencialogica:
    n = int(input())
    a=0
    
    if(n>1 and n<1000):
        for i in range(1,n+1):
            for k in range(1,4):
                print('{} {} {}'.format(i, i*i, i*i*i))
                break
            for j in range(1,4):
                if (j!=2 or j!=3):
                    print('{} {} {}'.format(i, i*i+1, i*i*i+1))
                    break
