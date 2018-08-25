a = 7
for i in range(1,10):
    b = a
    for j in range(1,4):    
        if(i%2!=0):
            print("I={} J={}".format(i,b))
        b-=1
    a+=1