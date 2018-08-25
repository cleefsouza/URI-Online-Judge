class teste1035:
	linha = input().split(' ')
	a, b, c, d = int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3])
	
	if(b>c and d>a and ((c+d)>(a+b)) and c>=0 and d>=0 and (a%2==0)):
		print('Valores aceitos')
	else:
		print('Valores nao aceitos')
