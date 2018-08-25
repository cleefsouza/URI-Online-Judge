class multiplos1044:
	linha = input().split(' ')
	
	a, b = int(linha[0]), int(linha[1])
	
	if(b>a):
		aux = a
		a = b
		b = aux
		
	if(a%b==0):
		print('Sao Multiplos')
	else:
		print('Nao sao Multiplos')
