n = int(input())
x, y = 0, 0
for i in range(0,n):
    x, y = [int(i) for i in input().split(" ")]
    if(x>y):
        aux=x
        x=y
        y=aux

    soma = 0
    for j in range(x+1,y):
        if(j%2!=0):
            soma+=j
    print(soma)