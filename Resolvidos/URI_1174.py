x = []
for i in range(100):
    n = input()
    x.append(float(n))
    if(x[i]<=10):
        print("A[{}] = {:.1f}".format(i,x[i]))
