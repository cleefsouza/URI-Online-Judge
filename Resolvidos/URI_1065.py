par = 0
for i in range(5):
    n = int(input())
    if(n%2==0):
        par+=1
print('{} valores pares'.format(par))