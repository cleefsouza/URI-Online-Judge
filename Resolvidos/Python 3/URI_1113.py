c = 0
while(c<1):
    x, y = [int(i) for i in input().split(" ")]
    if(x == y):
        c+=1
    else:
        if(x>y):
            print("Decrescente")
        else:
            print("Crescente")