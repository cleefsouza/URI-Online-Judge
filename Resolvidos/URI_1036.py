class bhaskara1036:
	from math import sqrt
	
	linha = input().split(' ')
	a, b, c = float(linha[0]), float(linha[1]), float(linha[2])

	delta = ((pow(b,2)) - (4*a)*c)
	
	if(delta>=0 and a!=0):
		delta_raiz = sqrt(delta)
		divisor = 2*a

		x_1 = ((-b)+delta_raiz)/divisor
		x_2 = ((-b)-delta_raiz)/divisor
		
		print('R1 = {:.5f}'.format(x_1, end='\n'))
		print('R2 = {:.5f}'.format(x_2, end='\n'))

	else:
		print('Impossivel calcular',end='\n')
