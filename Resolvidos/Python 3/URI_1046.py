class tempojogo1046:
	horas = input().split(' ')
	
	inicio, fim = int(horas[0]), int(horas[1])
	hora_total = 0
	
	if(inicio<fim):
		hora_total = fim-inicio
	elif(inicio>fim):
		fim+=24
		hora_total = inicio-fim
		hora_total*=-1
	elif(inicio==fim):
		hora_total = 24

	if(hora_total>=1 and hora_total<=24):
		print('O JOGO DUROU {} HORA(S)'.format(hora_total))
