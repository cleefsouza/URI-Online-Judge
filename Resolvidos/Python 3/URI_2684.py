for i in range(int(input())):
    x = []
    
    for m in range(3):
        y = [int(n) for n in input().split(" ")]
        x.append(y)

    z = []
    for o in range(3):
        c = 0
        for p in range(3):
            if(c==0):
                cc = (x[o][p]-x[o][p+1])
                if(cc<0):
                    cc*=-1
                z.append(cc)
                c+=1
            elif(c==1):
                cc = (x[o][p]-x[o][p-1])
                if(cc<0):
                    cc*=-1
                z.append(cc)
                c+=1
            elif(c==2):
                cc = (x[o][p]-x[o][p-1])
                if(cc<0):
                    cc*=-1
                z.append(cc)

    maior = 0
    for i in z:
        if(z.count(i)>z.count(maior)):
            maior=i

    w = []
    for q in range(3):
        c = 0
        for r in range(3):
            if(c==0):
                x1, x2 = (x[q][r]-x[q][r+1]), (x[q][r]-x[q][r+2])
                if(x1<0):
                    x1 = x1*(-1)
                if(x2<0):
                    x2 = x2*(-1)

                if(x1!=maior and x2!=maior):
                    w.append(x[q][r])
            elif(c==1):
                x1, x2 = (x[q][r]-x[q][r-1]), (x[q][r]-x[q][r+1])
                if(x1<0):
                    x1 = x1*(-1)
                if(x2<0):
                    x2 = x2*(-1)

                if(x1!=maior and x2!=maior):
                    w.append(x[q][r])
            elif(c==2):
                x1, x2 = (x[q][r]-x[q][r-2]), (x[q][r]-x[q][r-1])
                if(x1<0):
                    x1 = x1*(-1)
                if(x2<0):
                    x2 = x2*(-1)

                if(x1!=maior and x2!=maior):
                    w.append(x[q][r])
            c+=1
    resu = str(w)[1:-1]
    print("Possiveis maletas: {};".format(resu))
