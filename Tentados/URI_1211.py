while True:
    try:
        x = []
        y = []
        for i in range(int(input())):
            x.append(input())

        for j in x:
            if(j != x[0]):
                jj = 0
                for z in j:
                    if(z==x[0][jj]):
                        y.append(z)
                    jj+=1
        
        print(len(y))

    except EOFError:
        break