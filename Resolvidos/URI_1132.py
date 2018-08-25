class multiplos13:
    x = int(input())
    y = int(input())
    
    
    if(x>y):
        aux = x
        x = y
        y = aux
        
    co1 = 0
    for i in range(x,y+1):
        if(i%13!=0):
            co1 += i
        
    print(co1)
