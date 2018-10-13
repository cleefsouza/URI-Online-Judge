lixo,d1 = input().split(" ")
h1,lixo,m1,lixo,s1 = input().split(" ")

lixo,d2 = input().split(" ")
h2,lixo,m2,lixo,s2 = input().split(" ")

q1 = int(s1) + int(m1)*60 + int(h1) * 60 * 60 + int(d1) * 60 * 60 * 24
q2 = int(s2) + int(m2)*60 + int(h2) * 60 * 60 + int(d2) * 60 * 60 * 24
tempo = q2-q1 
dia = tempo//(60*60*24)
tempo = tempo%(60*60*24)
horas = tempo//(60*60)
tempo = tempo%(60*60)
minutos =tempo//(60)
tempo = tempo%(60)
print("{} dia(s)".format(dia))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(tempo))