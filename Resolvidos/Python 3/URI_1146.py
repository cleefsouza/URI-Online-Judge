while True:
    x = int(input())
    if(x!=0):
        for i in range(1, x+1):
            if(i==x):
                print(i, end="\n")
            else:
                print(i, end=" ")
    else:
        break
