class lanche1038:
	linha = input().split(' ')
	
	cod ,qtd = int(linha[0]), int(linha[1])
	
	if(cod==1):
		preco = float(qtd*4)
		print('Total: R$ {:.2f}'.format(preco))
	elif(cod==2):
		preco = float(qtd*4.50)
		print('Total: R$ {:.2f}'.format(preco))
	elif(cod==3):
		preco = float(qtd*5)
		print('Total: R$ {:.2f}'.format(preco))
	elif(cod==4):
		preco = float(qtd*2)
		print('Total: R$ {:.2f}'.format(preco))
	elif(cod==5):
		preco = float(qtd*1.5)
		print('Total: R$ {:.2f}'.format(preco))
