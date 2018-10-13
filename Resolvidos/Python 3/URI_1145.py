x,y = list(map(int,input().split()))
c = 1
for i in range(1,(int((y/x))+1)):
    r = ""
    for y in range(x):
        r += str(c) + " "
        c += 1
    print(r[:-1])