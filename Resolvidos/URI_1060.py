class positivo1060:
	n = []
	pos = 0
	for i in range(6):
		n.append(float(input()))
		if(n[i]>0):
			pos+=1
	
	print('{} valores positivos'.format(pos))