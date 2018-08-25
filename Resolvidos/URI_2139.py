while True:
    try:
        m, d = [int(i) for i in input().split(" ")]
        jan, fev, mar, abr, mai, jun, jul, ago, sete, out, nov = 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30

        if(m==12):
            if(d<24):
                print("Faltam {} dias para o natal!".format(25-d))
            elif(d==24):
                print("E vespera de natal!")
            elif(d==25):
                print("E natal!")
            else:
                print("Ja passou!")
        
        if(m==11):
            print("Faltam {} dias para o natal!".format(nov-d+25))
        elif(m==10):
            print("Faltam {} dias para o natal!".format(nov+out-d+25))
        elif(m==9):
            print("Faltam {} dias para o natal!".format(nov+out+sete-d+25))
        elif(m==8):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago-d+25))
        elif(m==7):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul-d+25))
        elif(m==6):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul+jun-d+25))
        elif(m==5):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul+jun+mai-d+25))
        elif(m==4):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul+jun+mai+abr-d+25))
        elif(m==3):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul+jun+mai+abr+mar-d+25))
        elif(m==2):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul+jun+mai+abr+mar+fev-d+25))
        elif(m==1):
            print("Faltam {} dias para o natal!".format(nov+out+sete+ago+jul+jun+mai+abr+mar+fev+jan-d+25))

    except EOFError:
        break
