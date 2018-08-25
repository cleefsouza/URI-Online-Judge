class triangulo1043:
	linha = input().split(' ')
	
	a, b, c = float(linha[0]), float(linha[1]), float(linha[2])
	
	if ((c-b)<a<(c+b))and((b-a)<c<(b+a))and((c-a)<b<(c+a)):
		p = a+b+c
		print('Perimetro = {:.1f}'.format(p))
	else:
		a = ((a+b)*c)/2
		print('Area = {:.1f}'.format(a))
