for i in range(int(input())):
    s = 0
    for j in range(1,int(input())+1):
        if(j%2!=0):
            s = s-1
        else:
            s = s+1
    print(s*-1)
