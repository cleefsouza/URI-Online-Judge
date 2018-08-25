class intervalo1037:
	n = float(input())
	
	if(n>75 and n<=100):
		print('Intervalo (75,100]')
	elif(n>50 and n<75):
		print('Intervalo (50,75]')
	elif(n>25 and n<=50.0000000):
		print('Intervalo (25,50]')
	elif(n>=0 and n<=25.0000):
		print('Intervalo [0,25]')
	elif(n<0 or n>100):
		print('Fora de intervalo')
