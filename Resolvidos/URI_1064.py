c = 0
media = 0
for i in range(6):
    n = float(input())
    if(n>0):
        c+=1
        media += n
print('{} valores positivos'.format(c))
print('{:.1f}'.format(media/c))