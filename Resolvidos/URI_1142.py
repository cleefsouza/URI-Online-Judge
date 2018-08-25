n = int(input())
c= 0
for i in range(0, n):
    for j in range(1, 5):
        c+=1
        if(c%4==0):
            print('PUM')
        else:
            print(c, end=' ')
