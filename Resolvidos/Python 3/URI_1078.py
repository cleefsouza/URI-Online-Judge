class tabuada:
    num = int(input())
    cont = 1
    
    if(num>2 and num<1000):
        while(cont!=11):
            resu = num*cont
            print('{} x {} = {}'.format(cont,num,resu))
            cont = cont+1
