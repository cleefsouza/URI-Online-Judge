n = []
x = []
for i in range(2):
    n.append(int(input()))

if(n[0]>n[1]):
    aux = n[0]
    n[0] = n[1]
    n[1] = aux

for i in range(n[0]+1,n[1]):
    if(i%5==2 or i%5==3):
        x.append(int(i))

for j in x:
    print(j)
