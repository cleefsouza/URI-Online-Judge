i, j = 1, 7
while(i<=9):
    while(j>=5):
        if(i%2!=0):
            print('I={} J={}'.format(i, j))
        j-=1
    j = 7
    i+=1