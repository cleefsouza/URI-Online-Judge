verifica = 1
grenais, inter, gremio, empates = 0, 0, 0, 0
while True:
    gols = [int(i) for i in input().split(" ")]

    grenais+=1
    if(gols[0]>gols[1]):
        inter+=1
    elif(gols[0]<gols[1]):
        gremio+=1
    else:
        empates+=1

    print("Novo grenal (1-sim 2-nao)")
    verifica = int(input())

    if(verifica==2):
        break
print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empates))
if(inter>gremio):
    print("Inter venceu mais")
elif(inter<gremio):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
