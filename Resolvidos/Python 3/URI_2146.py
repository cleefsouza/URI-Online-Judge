class senha:
    while True:
        try:
            senha = int(input())
            if(senha>=1001 and senha<=9999):
                senha=senha-1
                print(senha)
        except :
            break