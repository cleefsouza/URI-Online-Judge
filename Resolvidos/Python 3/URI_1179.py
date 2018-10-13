x, y = [], []
for i in range(15):
    n = int(input())
    if(n%2==0):
        x.append(n)
    else:
        y.append(n)

    if(len(x)==5):
        for j in range(5):
            print("par[{}] = {}".format(j, x[j]))
        x = []
        
    if(len(y)==5):
        for j in range(5):
            print("impar[{}] = {}".format(j, y[j]))
        y = []

for k in range(len(y)):
    print("impar[{}] = {}".format(k, y[k]))

for l in range(len(x)):
    print("par[{}] = {}".format(l, x[l]))
