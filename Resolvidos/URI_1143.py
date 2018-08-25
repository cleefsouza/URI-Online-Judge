n = int(input())
c = 1
for i in range(0, n):
    for j in range(1, 4):
        if(j!=3):
            print(pow(c,j), end=' ')
        else:
            print(pow(c,j), end='\n')
    c+=1
