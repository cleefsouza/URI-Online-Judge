c = 0
while(c<1):
    x, y = [int(i) for i in input().split(" ")]
    if(x==0 or y==0):
        c+=1
    else:
        if(x > 0 and y > 0):
            print("primeiro")
        elif(x > 0 and y < 0):
            print("quarto")
        elif(x < 0 and y > 0):
            print("segundo")
        elif(x < 0 and y < 0):
            print("terceiro")