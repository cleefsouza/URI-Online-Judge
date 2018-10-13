while True:
    try:
        n = int(input())
        if(n == 0):
            break
        resu = []
        
        for i in range(1,n+1):
            v, c = [], i
            for j in range(n):
                v.append(abs(c))
                if(c == 1):
                    c-=3
                else:
                    c-=1
            resu.append(v)

        for i in range(n):
            tx = ''
            for j in range(n):
                tx+=" %3d"%resu[i][j]
            print(tx[1:])
        print()
    except:
        break
