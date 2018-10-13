par = impar = posi = nega = 0
for i in range(5):
    n = int(input())
    if(n%2==0):
        par+=1
    elif(n%2!=0):
        impar+=1
    
    if(n>0):
        posi+=1
    elif(n<0):
        nega+=1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(posi))
print('{} valor(es) negativo(s)'.format(nega))