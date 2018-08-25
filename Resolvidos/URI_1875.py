c = int(input())
for i in range(0, c):
    p = int(input())
    G = 0
    R = 0
    B = 0
    for j in range(0, p):
        gols = input().split(" ")
        if(gols[0]=="R" and gols[1]=="G"):
            R+=2
        elif(gols[0]=="R" and gols[1]=="B"):
            R+=1
        elif(gols[0]=="G" and gols[1]=="R"):
            G+=1
        elif(gols[0]=="G" and gols[1]=="B"):
            G+=2
        elif(gols[0]=="B" and gols[1]=="G"):
            B+=1
        elif(gols[0]=="B" and gols[1]=="R"):
            B+=2
        
    if(B == G and B == R):
        print("trempate")
    elif((B == G and B > R) or (B == R and B > G)):
        print("empate")
    elif(G == R and G > B):
        print("empate")

    if(B > G and B > R):
        print("blue")
    elif(G > B and G > R):
        print("green")
    elif(R > G and R > B):
        print("red")