class tempojogo21047:
	tempo = input().split(' ')
	
	hinicio, minicio, hfim, mfim = int(tempo[0]), int(tempo[1]), int(tempo[2]), int(tempo[3])
	
	hora_total = hfim - hinicio
	minu_total = mfim - minicio
	
	if(hora_total<=0):
		hora_total += 24
	
	if(minu_total<0):
		hora_total -= 1
		minu_total += 60
	
	if(hinicio == hfim and minicio == mfim):
		print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora_total, minu_total))
	else:
		print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora_total, minu_total))
