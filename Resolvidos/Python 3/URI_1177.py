t = int(input())
x = 0    
for i in range(1000):
    print("N[{}] = {}".format(i, x))
    if(x<(t-1)):
        x+=1
    else:
        x=0
