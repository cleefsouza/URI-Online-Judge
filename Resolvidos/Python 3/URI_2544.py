while True:
    try:
        num = int(input())
        cont = 0
        while(num >= 2):
            num = num/2
            cont+=1
        print(cont)
    except:
        break
