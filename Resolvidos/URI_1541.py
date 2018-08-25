import math
c = 1
while True:
    linha = input().split(" ")
    if(linha[0]=="0"):
        break
    else:
        c, a, b = int(linha[0]), int(linha[1]), int(linha[2])
        x = c*a
        y = 100.0/b
        z = x*y
        w = int(math.sqrt(z))
        print("{}".format(w))