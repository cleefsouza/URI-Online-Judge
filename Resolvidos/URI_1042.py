class sortsimples1042:
	linha = input().split(' ')
	a, b, c = int(linha[0]), int(linha[1]), int(linha[2])
	
	lista = [a, b, c]
	lista.sort()
	
	print('{}\n{}\n{}'.format(lista[0], lista[1], lista[2]))
	print()
	print('{}\n{}\n{}'.format(a, b, c))
