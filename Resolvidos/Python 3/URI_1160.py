for i in range(int(input())):
    lista = input().split(" ")
    pa, pb, g1, g2 = int(lista[0]), int(lista[1]), float(lista[2]), float(lista[3])

    ano, cpa, cpb = 0, 0, 0        
    
    while True:
        cpa = int(pa+(pa*(g1/100)))
        cpb = int(pb+(pb*(g2/100)))
        pa = cpa
        pb = cpb
        ano+=1
        if(pa>pb and ano<=100):
            print("{:.0f} anos.".format(ano))
            break
        elif(ano>100):
            print("Mais de 1 seculo.")
            break
