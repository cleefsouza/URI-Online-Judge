while True:
    n = int(input())
    if(n==0):
        break
    elif(n==1):
        print(n)
        print()
    elif(n==2):
        print("1 2\n2 4")
        print()
    else:
        x, c = [], 1
        for i in range(n):
            y = []
            for j in range(1,n+1):
                y.append(c)
                c*=2
            x.append(y)
            c = x[i][1]
        c = 0
        s = len(str(x[i][j-1]))
        for k in range(n):
            for m in range(n):
                if(m<(n-1)):
                    print("{:{}}".format(x[k][m],s), end=" ")
                else:
                    print("{:{}}".format(x[k][m],s), end="\n")
        print()
