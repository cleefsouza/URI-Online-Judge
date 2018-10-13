class cedulas1018:
    n = int(input())
    
    n100 = 0
    n50 = 0
    n20 = 0
    n10 = 0
    n5 = 0
    n2 = 0
    n1 = 0
    
    if(n>0 and n<1000000):
        print(n)
        while(n>=100):
            n100=n100+1
            n=n-100
        while(n>=50 and n<100):
            n50=n50+1
            n=n-50
        while(n>=20 and n<50):
            n20=n20+1
            n=n-20
        while(n>=10 and n<20):
            n10=n10+1
            n=n-10
        while(n>=5 and n<10):
            n5=n5+1
            n=n-5
        while(n>=2 and n<5):
            n2=n2+1
            n=n-2
        while(n>=1 and n<2):
            n1=n1+1
            n=n-1
        
        print(n100,'nota(s) de R$ 100,00')
        print(n50,'nota(s) de R$ 50,00')
        print(n20,'nota(s) de R$ 20,00')
        print(n10,'nota(s) de R$ 10,00')
        print(n5,'nota(s) de R$ 5,00')
        print(n2,'nota(s) de R$ 2,00')
        print(n1,'nota(s) de R$ 1,00')
