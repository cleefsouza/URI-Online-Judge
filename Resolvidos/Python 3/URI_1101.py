c = 0
while(c<1):
    n, m = [int(i) for i in input().split(" ")]
    if(m > 0 and n > 0):
        if(m<n):
            aux=n
            n=m
            m=aux
        
        num = []
        res = 0
        soma = 0
        for i in range(n, m+1):
            num.append(i)
            res = " ".join(map(str, num))
            soma = sum(num)
        print(res, "Sum=%i" %soma)
        num = []
    else:
        c+=1