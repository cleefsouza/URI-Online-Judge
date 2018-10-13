class cachorroquente:
	qtd = input().split(' ')
	n,m = int(qtd[0]), int(qtd[1])
	
	if(1<=n,m<=1000):
		r = float((n/m))
		print('{:.2f}'.format(r))
