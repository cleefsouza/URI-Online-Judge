cont = 0
while(True):
    try:
        n = int(input())
        num = 1
        cont+=1
        num+=((n*(n+1))/2)

        if(n==0):
            print("Caso %d: %d numero"%(cont, num))
        else:
            print("Caso %d: %d numeros"%(cont, num))

        numero = "0 "
        for i in range(1, n+1):
            for j in range(0, i):
                numero+=str(i)+" "

        print(numero[:-1])
        print()

    except EOFError:
        break
        print()
