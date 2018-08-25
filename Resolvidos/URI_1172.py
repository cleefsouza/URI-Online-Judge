x = []
for i in range(10):
    n = int(input())
    if(n<=0):
        n=1
    x.append(n)
    print("X[{}] = {}".format(i,x[i]))
