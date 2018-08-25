class idadeemdias1020:
    i = int(input())
    
    a = 0
    m = 0
    d = 0
    
    while(i>0):
        while(i>=365):
            a+=1
            i-=365
        while(i>=30 and i<365):
            m+=1
            i-=30
        while(i>=1 and i<30):
            d+=1
            i-=1
    
    print(a,'ano(s)')
    print(m,'mes(es)')
    print(d,'dia(s)')
