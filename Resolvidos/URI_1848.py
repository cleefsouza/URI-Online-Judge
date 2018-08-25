g, n = 0, 0
while(g<3):
    s = input()
    if(s=="---"):
        n+=0
    elif(s=="*--"):
        n+=4
    elif(s=="**-"):
        n+=6
    elif(s=="***"):
        n+=7
    elif(s=="--*"):
        n+=1
    elif(s=="-**"):
        n+=3
    elif(s=="*-*"):
        n+=5
    elif(s=="-*-"):
        n+=2
    else:
        print(n)
        g+=1
        n=0
